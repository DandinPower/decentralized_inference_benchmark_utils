#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <thread>
#include <zmq.hpp>
#include <zmq_addon.hpp> 

// -------------------------------------------------------------------------
// HELPER: ISO 8601 Timestamp
// -------------------------------------------------------------------------
std::string get_iso8601_timestamp() {
    using namespace std::chrono;
    auto now = system_clock::now();
    auto ms = duration_cast<milliseconds>(now.time_since_epoch()) % 1000;
    std::time_t now_c = system_clock::to_time_t(now);
    std::tm* tm_ptr = std::gmtime(&now_c);
    std::stringstream ss;
    ss << std::put_time(tm_ptr, "%Y-%m-%dT%H:%M:%S");
    ss << "." << std::setfill('0') << std::setw(3) << ms.count() << "Z";
    return ss.str();
}

long long parse_iso_to_epoch_ms(const std::string& iso_str) {
    int y, M, d, h, m, s, ms;
    if (sscanf(iso_str.c_str(), "%d-%d-%dT%d:%d:%d.%dZ", &y, &M, &d, &h, &m, &s, &ms) != 7) return 0; 
    std::tm tm = {};
    tm.tm_year = y - 1900; tm.tm_mon = M - 1; tm.tm_mday = d;
    tm.tm_hour = h; tm.tm_min = m; tm.tm_sec = s; tm.tm_isdst = 0;
    time_t t = timegm(&tm); 
    return (long long)t * 1000 + ms;
}

// -------------------------------------------------------------------------
// HELPER: Send Payload
// Encapsulates the logic to create and send the 6-frame message
// -------------------------------------------------------------------------
void send_payload(zmq::socket_t& socket, const std::string& key, size_t buffer_size) {
    std::string type = "f32"; 
    int64_t dims[2] = {1, (int64_t)buffer_size}; 
    int64_t size_info = buffer_size;
    
    // We allocate the buffer every time to ensure the test is fair (memory access overhead included)
    std::vector<char> dummy_data(buffer_size, 'A'); 

    // 1. Capture Start Time
    std::string start_time_str = get_iso8601_timestamp();
    std::cout << "[" << key << "] send start: " << start_time_str << std::endl;

    // 2. Build Message
    std::vector<zmq::message_t> msgs;
    msgs.emplace_back(key.data(), key.size());
    msgs.emplace_back(type.data(), type.size());
    msgs.emplace_back(dims, sizeof(dims));
    msgs.emplace_back(dummy_data.data(), buffer_size);
    msgs.emplace_back(&size_info, sizeof(size_info));
    msgs.emplace_back(start_time_str.data(), start_time_str.size());

    // 3. Send
    try {
        zmq::send_multipart(socket, msgs);
    } catch (const zmq::error_t& e) {
        std::cerr << "Failed to send: " << e.what() << std::endl;
    }

    std::string stop_time_str = get_iso8601_timestamp();
    std::cout << "[" << key << "] send stop:  " << stop_time_str << std::endl;
}

// -------------------------------------------------------------------------
// SENDER
// -------------------------------------------------------------------------
void run_sender(const std::string& next_node_ip, int next_node_port, size_t buffer_size) {
    zmq::context_t ctx(1);
    zmq::socket_t socket(ctx, zmq::socket_type::push);
    
    // Disable linger to ensure we rely on explicit application flow, 
    // BUT since we sleep at the end, default linger is also fine.
    // socket.set(zmq::sockopt::linger, 0); 

    std::string endpoint = "tcp://" + next_node_ip + ":" + std::to_string(next_node_port);
    std::cout << "[Sender] Connecting to " << endpoint << "..." << std::endl;
    socket.connect(endpoint);

    // --- STEP 1: WARMUP (Full Size) ---
    std::cout << "\n[Sender] === STARTING WARMUP (" << buffer_size << " bytes) ===" << std::endl;
    send_payload(socket, "warmup", buffer_size);

    // Wait for the receiver to digest the warmup and print stats.
    // This pause also ensures the TCP window opens up and stabilizes.
    std::cout << "[Sender] Pausing 3 seconds for stabilization..." << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(3000));

    // --- STEP 2: REAL DATA (Full Size) ---
    std::cout << "\n[Sender] === STARTING BENCHMARK (" << buffer_size << " bytes) ===" << std::endl;
    send_payload(socket, "benchmark_tensor", buffer_size);
    
    // Give time for socket to flush before context destruction
    std::this_thread::sleep_for(std::chrono::milliseconds(500));
}

// -------------------------------------------------------------------------
// RECEIVER
// -------------------------------------------------------------------------
void run_receiver(int listen_port) {
    zmq::context_t ctx(1);
    zmq::socket_t socket(ctx, zmq::socket_type::pull);
    
    std::string endpoint = "tcp://*:" + std::to_string(listen_port);
    std::cout << "[Receiver] Binding to " << endpoint << "..." << std::endl;
    socket.bind(endpoint);

    std::cout << "[Receiver] Waiting for data..." << std::endl;

    while (true) {
        std::vector<zmq::message_t> recv_msgs;
        
        try {
            auto res = zmq::recv_multipart(socket, std::back_inserter(recv_msgs));
            if (!res) continue;
        } catch (const zmq::error_t& e) {
            std::cerr << "Recv error: " << e.what() << std::endl;
            break;
        }

        // 1. Capture Recv Stop immediately
        std::string recv_stop_str = get_iso8601_timestamp();
        std::string key = recv_msgs[0].to_string();

        std::cout << "\n------------------------------------------------" << std::endl;
        std::cout << "RECEIVED PAYLOAD TYPE: " << key << std::endl;
        std::cout << "recv stop: " << recv_stop_str << std::endl;

        // 2. Calculate Statistics
        if (recv_msgs.size() >= 6) {
            size_t payload_bytes = recv_msgs[3].size();
            std::string sender_start_str = recv_msgs[5].to_string();
            
            long long t_send_start = parse_iso_to_epoch_ms(sender_start_str);
            long long t_recv_stop  = parse_iso_to_epoch_ms(recv_stop_str);
            long long latency_ms = t_recv_stop - t_send_start;

            std::cout << "Sender Start: " << sender_start_str << std::endl;
            std::cout << "Latency:      " << latency_ms << " ms" << std::endl;
            
            if (latency_ms > 0) {
                double latency_sec = latency_ms / 1000.0;
                double bw_mbps = (payload_bytes * 8.0) / (latency_sec * 1e6); // Megabits per sec
                double bw_gbps = (payload_bytes * 8.0) / (latency_sec * 1e9); // Gigabits per sec
                
                std::cout << "Throughput:   " << std::fixed << std::setprecision(2) << bw_mbps << " Mbps" << std::endl;
                std::cout << "Throughput:   " << std::fixed << std::setprecision(2) << bw_gbps << " Gbps" << std::endl;
            } else {
                std::cout << "Throughput:   Inf (Latency < 1ms or clock skew)" << std::endl;
            }
        } else {
            std::cerr << "Error: Invalid multipart format." << std::endl;
        }
        std::cout << "------------------------------------------------" << std::endl;

        // 3. Logic Control
        if (key == "benchmark_tensor") {
            std::cout << "[Receiver] Benchmark complete. Exiting." << std::endl;
            break; 
        } else if (key == "warmup") {
            std::cout << "[Receiver] Warmup done. Waiting for next..." << std::endl;
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;
    std::string mode = argv[1];
    if (mode == "send" && argc == 5) run_sender(argv[2], std::stoi(argv[3]), std::stoul(argv[4]));
    else if (mode == "recv" && argc == 3) run_receiver(std::stoi(argv[2]));
    else return 1;
    return 0;
}