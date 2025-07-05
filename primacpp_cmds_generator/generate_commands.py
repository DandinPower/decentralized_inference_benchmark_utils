import json
from argparse import ArgumentParser, Namespace
from pathlib import Path

from utils import validate_fields


def generate_master_nodes_cmd(configs: dict, prompt: str) -> str:
    validate_fields(configs, "master_node", expected_type=dict)
    master_node = configs.get("master_node")

    validate_fields(master_node, "loopback_ip", "public_ip", expected_type=str)
    validate_fields(master_node, "layer_window_size", "data_port",
                    "signal_port", "public_data_port", "public_signal_port", expected_type=int)

    mode = configs.get('mode')
    if mode == "server":
        validate_fields(master_node, "server_host", expected_type=str)
        validate_fields(master_node, "server_port",
                        "number_process", expected_type=int)

    validate_fields(configs, "server_nodes", expected_type=list)
    server_nodes = configs.get("server_nodes")
    world_size = 1 + len(server_nodes)
    assert world_size >= 2, f"World size must be at least 2, but got {world_size}."
    next_node = server_nodes[0]
    validate_fields(next_node, "public_ip", expected_type=str)
    validate_fields(next_node, "layer_window_size", "data_port", "signal_port",
                    "public_data_port", "public_signal_port", expected_type=int)

    layer_windows = [master_node.get("layer_window_size")]
    for server in server_nodes:
        validate_fields(server, "layer_window_size", expected_type=int)
        layer_windows.append(server.get("layer_window_size"))
    layer_windows = ",".join(map(str, layer_windows))

    if mode == "server":
        args = ["./llama-server"]
        args += ["-m", configs.get("gguf_file")]
        args += ["--host", master_node.get("server_host"),
                 "--port", master_node.get("server_port"),
                 "-c", configs.get("ctx_size"),
                 "-b", configs.get("n_batch"),
                 "-ub", configs.get("n_ubatch"),
                 "-np", master_node.get("number_process")]
        args += ["--world", world_size,
                 "--rank", 0,
                 "-lw", layer_windows,
                 "-ngl", master_node.get("layer_window_size"),
                 "--data_port", master_node.get("data_port"),
                 "--signal_port", master_node.get("signal_port"),
                 "--master", master_node.get("loopback_ip"),
                 "--master_data_port", master_node.get("data_port"),
                 "--next", next_node.get("public_ip"),
                 "--next_node_data_port", next_node.get("public_data_port"),
                 "--next_node_signal_port", next_node.get(
                     "public_signal_port"),
                 ]
        if master_node.get("splits") is not None:
            args += ["--splits", master_node.get("splits")]
        if master_node.get("additional_flags") is not None:
            args += [master_node.get("additional_flags")]
    else:
        args = ["./llama-cli"]
        args += ["-m", configs.get("gguf_file")]
        args += ["-c", configs.get("ctx_size"),
                 "-n", configs.get("n_predict"),
                 "-p", f"\"{prompt}\""]
        args += ["--world", world_size,
                 "--rank", 0,
                 "-lw", layer_windows,
                 "-ngl", master_node.get("layer_window_size"),
                 "--data_port", master_node.get("data_port"),
                 "--signal_port", master_node.get("signal_port"),
                 "--master", master_node.get("loopback_ip"),
                 "--master_data_port", master_node.get("data_port"),
                 "--next", next_node.get("public_ip"),
                 "--next_node_data_port", next_node.get("public_data_port"),
                 "--next_node_signal_port", next_node.get(
                     "public_signal_port"),
                 ]

        if master_node.get("splits") is not None:
            args += ["--splits", master_node.get("splits")]
        if master_node.get("additional_flags") is not None:
            args += [master_node.get("additional_flags")]

    return " ".join(map(str, args))


def generate_server_nodes_cmds(configs: dict) -> list[str]:
    def _build_server_cmd(configs: dict, rank: int, current_node: dict, next_node: dict) -> str:
        master_node = configs.get("master_node")
        world_size = 1 + len(configs.get("server_nodes"))
        args = ["./llama-cli"]
        args += ["-m", configs.get("gguf_file")]
        args += ["--world", world_size,
                 "--rank", rank,
                 "-ngl", current_node.get("layer_window_size"),
                 "--data_port", current_node.get("data_port"),
                 "--signal_port", current_node.get("signal_port"),
                 "--master", master_node.get("public_ip"),
                 "--master_data_port", master_node.get("public_data_port"),
                 "--next", next_node.get("public_ip"),
                 "--next_node_data_port", next_node.get("public_data_port"),
                 "--next_node_signal_port", next_node.get(
                     "public_signal_port"),
                 ]

        if current_node.get("splits") is not None:
            args += ["--splits", current_node.get("splits")]
        if current_node.get("additional_flags") is not None:
            args += [current_node.get("additional_flags")]

        return " ".join(map(str, args))

    master_node = configs.get("master_node")
    all_server_nodes = configs.get("server_nodes")

    cmds = []
    for idx, current_node in enumerate(all_server_nodes):
        next_node = master_node if idx == len(
            all_server_nodes)-1 else all_server_nodes[idx+1]

        validate_fields(current_node, "layer_window_size", "data_port", "signal_port",
                        "public_data_port", "public_signal_port", expected_type=int)
        validate_fields(current_node, "public_ip", expected_type=str)
        validate_fields(next_node, "layer_window_size", "data_port", "signal_port",
                        "public_data_port", "public_signal_port", expected_type=int)
        validate_fields(next_node, "public_ip", expected_type=str)

        cmds.append(_build_server_cmd(configs, rank=idx+1,
                    current_node=current_node, next_node=next_node))
    return cmds


def read_prompt_from_file(prompt_path: str) -> str:
    prompt_file = Path(prompt_path)
    if not prompt_file.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    if not prompt_file.suffix.lower() == ".txt":
        raise ValueError(
            f"Prompt file must have .txt extension: {prompt_path}")

    try:
        with open(prompt_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        prompt = " ".join(line.strip() for line in lines if line.strip())

        if not prompt:
            raise ValueError(
                f"Prompt file is empty or contains only whitespace: {prompt_path}")
        return prompt

    except Exception as e:
        raise RuntimeError(f"Error reading prompt file {prompt_path}: {e}")


def main(args: Namespace):
    cfg = Path(args.config_path)
    assert cfg.exists(), f"No such file: {cfg}"
    cfg_dict = json.loads(cfg.read_text(encoding="utf-8"))

    mode = cfg_dict.get("mode")
    assert mode == "server" or mode == "cli", f"Invalid mode: '{mode}'. Supported modes are 'server' or 'cli'."

    validate_fields(cfg_dict, "gguf_file", expected_type=str)
    validate_fields(cfg_dict, "ctx_size", "n_batch",
                    "n_ubatch", expected_type=int)

    if mode == "cli":
        validate_fields(cfg_dict, "n_predict", expected_type=int)
        prompt = read_prompt_from_file(args.prompt_path)
    else:
        prompt = None

    print("Master Node Command:")
    print("-"*60)
    print(generate_master_nodes_cmd(cfg_dict, prompt))
    print("-"*60)

    for i, cmd in enumerate(generate_server_nodes_cmds(cfg_dict)):
        print(f"Server {i} Node Command:")
        print(cmd)
        print("-"*60)


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("-c", "--config-path", required=True)
    p.add_argument("-p", "--prompt-path", required=False,
                   help="Path to .txt file containing the prompt (required for CLI mode)")
    main(p.parse_args())
