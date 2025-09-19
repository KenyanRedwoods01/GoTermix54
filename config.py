# gotermix54/config.py
import os
import json
from pathlib import Path

DEFAULT_CONFIG = {
    "ai": {
        "model": "auto",
        "mistral_api_key": "",
        "codestral_api_key": "",
        "endpoint": "https://api.mistral.ai/v1/chat/completions"
    },
    "system": {
        "confirm_dangerous": True,
        "verbose": False
    }
}

GLOBAL_CONFIG_PATH = Path.home() / ".gotermix54" / "config.json"
PROJECT_CONFIG_PATH = Path.cwd() / ".gotermix54" / "config.json"

def load_config():
    config = DEFAULT_CONFIG.copy()
    
    # Load global config
    if GLOBAL_CONFIG_PATH.exists():
        with open(GLOBAL_CONFIG_PATH, 'r') as f:
            global_conf = json.load(f)
            config = deep_merge(config, global_conf)
    
    # Load project config (overrides global)
    if PROJECT_CONFIG_PATH.exists():
        with open(PROJECT_CONFIG_PATH, 'r') as f:
            project_conf = json.load(f)
            config = deep_merge(config, project_conf)
    
    return config

def save_global_config(config):
    GLOBAL_CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(GLOBAL_CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=2)

def deep_merge(a, b):
    result = a.copy()
    for key, value in b.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result
