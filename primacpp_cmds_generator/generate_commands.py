import json
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Optional

def assert_int_fields(d: dict, *fields: str):
    for f in fields:
        assert isinstance(d.get(f), int), f"Invalid or missing integer field: {f}"

def build_master_cmd(
    gguf_file: str,
    ctx_size: int,
    world: int,
    rank: int,
    layer_windows: str,
    ngl: int,
    master_ip: str,
    data_port: int,
    signal_port: int,
    next_ip: str,
    master_data_port: int,
    next_data_port: int,
    next_signal_port: int,
    splits: Optional[str] = None,
    n_predict: Optional[int] = None,
    prompt: Optional[str] = None,
    server_host: Optional[str] = None,
    server_port: Optional[int] = None,
    number_process: Optional[int] = None
) -> str:
    if server_host:
        args = ["./llama-server"]
        args += ["--host", str(server_host)]
        args += ["--port", str(server_port)]
        if number_process:
            args += ["-np", str(number_process)]
    else:
        args = ["./llama-cli"]
        args += ["-n", str(n_predict)]
        args += ["-p", f'"{prompt}"']

    if splits:
        args += ["--splits", splits]

    args += [
        "-m", gguf_file,
        "-c", str(ctx_size),
        "--world", str(world),
        "--rank", str(rank),
        "--prefetch",
        "-lw", f'"{layer_windows}"',
        "-ngl", str(ngl),
        "--master", master_ip,
        "--data_port", str(data_port),
        "--signal_port", str(signal_port),
        "--next", next_ip,
        "--master_data_port", str(master_data_port),
        "--next_node_data_port", str(next_data_port),
        "--next_node_signal_port", str(next_signal_port),
    ]
    return " ".join(args)

def build_server_cmd(
    gguf_file: str,
    world: int,
    rank: int,
    ngl: int,
    master_ip: str,
    data_port: int,
    signal_port: int,
    next_ip: str,
    master_data_port: int,
    next_data_port: int,
    next_signal_port: int,
    splits: Optional[str] = None
) -> str: 
    args = ["./llama-cli"]
    if splits:
        args += ["--splits", splits]  

    args += [
        "-m", gguf_file,
        "--world", str(world),
        "--rank", str(rank),
        "--prefetch",
        "-ngl", str(ngl),
        "--master", master_ip,
        "--data_port", str(data_port),
        "--signal_port", str(signal_port),
        "--next", next_ip,
        "--master_data_port", str(master_data_port),
        "--next_node_data_port", str(next_data_port),
        "--next_node_signal_port", str(next_signal_port),
    ]
    return " ".join(args)

def generate_master_nodes_cmd(configs: dict, prompt: str, multi_splits: bool, server_mode: bool) -> str:
    m = configs['master_node']
    n = configs['server_nodes'][0]
    splits = m['splits'] if multi_splits else None

    # one‐time build of the full layer_windows string
    windows = [configs['master_node']['layer_window_size']] + [
        srv['layer_window_size'] for srv in configs['server_nodes']
    ]
    layer_windows = ",".join(map(str, windows))

    # validate common fields
    assert_int_fields(m, 'data_port','signal_port','public_data_port')
    assert_int_fields(n, 'public_data_port','public_signal_port')

    # validate server mode specific fields only when needed
    if server_mode:
        assert_int_fields(configs['master_node'], 'server_port')
        assert 'server_host' in configs['master_node'], "Missing server_host field"
        server_host = configs['master_node']['server_host']
        server_port = configs['master_node']['server_port']
        number_process = configs['master_node'].get('number_process')
        n_predict = None
        prompt_arg = None
    else:
        server_host = None
        server_port = None
        number_process = None
        n_predict = configs['n_predict']
        prompt_arg = prompt

    return build_master_cmd(
        gguf_file=configs['gguf_file'],
        ctx_size=configs['ctx_size'],
        world=configs['world'],
        rank=0,
        layer_windows=layer_windows,
        ngl=m['layer_window_size'],
        master_ip=m['loopback_ip'],
        data_port=m['data_port'],
        signal_port=m['signal_port'],
        next_ip=n['public_ip'],
        master_data_port=m['public_data_port'],
        next_data_port=n['public_data_port'],
        next_signal_port=n['public_signal_port'],
        splits=splits,
        n_predict=n_predict,
        prompt=prompt_arg,
        server_host=server_host,
        server_port=server_port,
        number_process=number_process
    )

def generate_server_nodes_cmds(configs: dict, multi_splits: bool) -> list[str]:
    m = configs['master_node']
    servers = configs['server_nodes']
    world = configs['world']
    splits_flag = multi_splits

    cmds = []
    for idx, srv in enumerate(servers, start=1):
        nxt = m if idx == world-1 else servers[idx]
        splits = srv['splits'] if splits_flag else None

        # validate
        assert_int_fields(srv, 'data_port','signal_port')
        assert_int_fields(m, 'public_data_port')
        assert_int_fields(nxt, 'public_data_port','public_signal_port')

        cmds.append(build_server_cmd(
            gguf_file   = configs['gguf_file'],
            world       = world,
            rank        = idx,
            ngl         = srv['layer_window_size'],
            master_ip   = m['public_ip'],
            data_port   = srv['data_port'],
            signal_port = srv['signal_port'],
            next_ip     = nxt['public_ip'],
            master_data_port = m['public_data_port'],
            next_data_port   = nxt['public_data_port'],
            next_signal_port = nxt['public_signal_port'],
            splits      = splits,
        ))

    return cmds

def read_prompt_from_file(prompt_path: str) -> str:
    """Read prompt from a text file and convert it to a single line."""
    prompt_file = Path(prompt_path)
    
    # Check if file exists
    if not prompt_file.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    
    # Check if file has .txt extension
    if not prompt_file.suffix.lower() == '.txt':
        raise ValueError(f"Prompt file must have .txt extension: {prompt_path}")
    
    # Read all lines and join them into a single line
    try:
        with open(prompt_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Strip whitespace from each line and join with space
        prompt = ' '.join(line.strip() for line in lines if line.strip())
        
        if not prompt:
            raise ValueError(f"Prompt file is empty or contains only whitespace: {prompt_path}")
        
        return prompt
    except Exception as e:
        raise RuntimeError(f"Error reading prompt file {prompt_path}: {e}")

def main(args: Namespace):
    cfg = Path(args.config_path)
    assert cfg.exists(), f"No such file: {cfg}"
    c = json.loads(cfg.read_text(encoding="utf-8"))

    assert c['world'] == 1 + len(c['server_nodes']), "World size mismatch"
    assert c['ctx_size'] >= 0
    
    # Only validate n_predict and read prompt for CLI mode
    if not args.server_mode:
        assert c['n_predict'] >= 0
        if not args.prompt_path:
            raise ValueError("--prompt-path is required for CLI mode")
        prompt = read_prompt_from_file(args.prompt_path)
    else:
        prompt = None

    print("Master Node Command:")
    print("-"*60)
    print(generate_master_nodes_cmd(c, prompt, args.multi_splits, args.server_mode))
    print("-"*60)

    for i, cmd in enumerate(generate_server_nodes_cmds(c, args.multi_splits)):
        print(f"Server {i} Node Command:")
        print(cmd)
        print("-"*60)

if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("--prompt-path", required=False, help="Path to .txt file containing the prompt (required for CLI mode)")
    p.add_argument("--config-path", required=True)
    p.add_argument("--multi-splits", action="store_true")
    p.add_argument("--server-mode", action="store_true")
    main(p.parse_args())
