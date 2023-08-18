import logging
import os
import yaml
from pathlib import Path
from typing import Dict, Any

logging.basicConfig()
logger = logging.getLogger("gke-service-sample")
logger.setLevel(logging.INFO)

def merge_config(
    base_config: Dict[str, Any],
    given_config: Dict[str, Any],
) -> Dict[str, Any]:
    for k, v in given_config.items():
        if isinstance(v, Dict):
            base_config[k] = merge_config(base_config.get(k, {}), v)
        else:
            base_config[k] = v
    return base_config

def get_config(
    env: str = os.getenv("ENV", "dev"),
    config_dpath: Path = Path(__file__).parent,
    config_type: str = "app"
):
    with open(config_dpath / f"{config_type}.yaml", "r", encoding="utf-8") as f:
        base_config = yaml.load(f, Loader=yaml.FullLoader)
        base_config["env"] = env
    override_fpath = config_dpath / f"{config_type}-{env}.yaml"
    if override_fpath.is_file():
        with open(override_fpath, "r", encoding="utf-8") as f:
            override_config = yaml.load(f, Loader=yaml.FullLoader) or {}
            return merge_config(base_config, override_config)
    else:
        return base_config

app_config = get_config()

__all__ = [
  "app_config",
  "logger"
]