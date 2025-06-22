import json
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Optional

def assert_int_fields(d: dict, *fields: str):
    for f in fields:
        assert isinstance(d.get(f), int), f"Invalid or missing integer field: {f}"

def build_llama_cmd(
    gguf_file: str,
    ctx_size: int,
    n_predict: int,
    prompt: str,
    world: int,
    rank: int,
    prefetch: bool,
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
) -> str:
    args = ["./llama-cli"]
    if splits:
        args += ["--splits", splits]

    args += [
        "-m", gguf_file,
        "-c", str(ctx_size),
        "-n", str(n_predict),
        "-p", f'"{prompt}"',
        "--world", str(world),
        "--rank", str(rank),
    ]
    if prefetch:
        args.append("--prefetch")

    args += [
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

def generate_node_cmd(
    configs: dict,
    node_cfg: dict,
    next_cfg: dict,
    rank: int,
    prompt: str,
    if_multi_splits: bool,
) -> str:
    # validations
    assert_int_fields(node_cfg, 'data_port', 'signal_port')
    assert_int_fields(next_cfg, 'public_data_port', 'public_signal_port')

    splits = node_cfg.get('splits') if if_multi_splits else None

    # build layer-window string once
    windows = [
        configs['master_node']['layer_window_size'],
        *[srv['layer_window_size'] for srv in configs['server_nodes']]
    ]
    layer_windows = ",".join(str(w) for w in windows)
    ngl = node_cfg["layer_window_size"]

    master_ip = (
        configs['master_node']['loopback_ip']
        if rank == 0
        else configs['master_node']['public_ip']
    )

    return build_llama_cmd(
        gguf_file=configs['gguf_file'],
        ctx_size=configs['ctx_size'],
        n_predict=configs['n_predict'],
        prompt=prompt,
        world=configs['world'],
        rank=rank,
        prefetch=True,
        layer_windows=layer_windows,
        ngl=ngl,
        master_ip=master_ip,
        data_port=node_cfg['data_port'],
        signal_port=node_cfg['signal_port'],
        next_ip=next_cfg['public_ip'],
        master_data_port=configs['master_node']['public_data_port'],
        next_data_port=next_cfg['public_data_port'],
        next_signal_port=next_cfg['public_signal_port'],
        splits=splits,
    )

def generate_master_nodes_cmd(configs: dict, prompt: str, if_multi_splits: bool) -> str:
    master = configs['master_node']
    next_node = configs['server_nodes'][0]
    return generate_node_cmd(configs, master, next_node, rank=0, prompt=prompt, if_multi_splits=if_multi_splits)

def generate_server_nodes_cmds(configs: dict, prompt: str, if_multi_splits: bool) -> list[str]:
    masters = configs['master_node']
    servers = configs['server_nodes']
    world = configs['world']
    return [
        generate_node_cmd(
            configs,
            srv,
            masters if idx + 1 == world - 1 else servers[idx + 1],
            rank=idx + 1,
            prompt=prompt,
            if_multi_splits=if_multi_splits,
        )
        for idx, srv in enumerate(servers)
    ]

def main(args: Namespace):
    cfg_path = Path(args.config_path)
    assert cfg_path.exists(), f"No such file: {cfg_path}"
    configs = json.loads(cfg_path.read_text(encoding="utf-8"))
    
    assert configs['world'] == 1 + len(configs['server_nodes']), "World size mismatch"
    assert configs['ctx_size'] >= 0 and configs['n_predict'] >= 0

    print("Master Node Command:")
    print("-" * 60)
    print(generate_master_nodes_cmd(configs, args.prompt, args.multi_splits))
    print("-" * 60)

    for i, cmd in enumerate(generate_server_nodes_cmds(configs, args.prompt, args.multi_splits)):
        print(f"Server {i} Node Command:")
        print(cmd)
        print("-" * 60)

if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("--prompt", required=True)
    p.add_argument("--config-path", required=True)
    p.add_argument("--multi-splits", action="store_true")
    main(p.parse_args())