import json
import os

file_name = "config.json"

def load_config():
    if not os.path.exists(file_name):
        default_config =  {"monthly_budget" : 0}
        save_config(default_config)
        return default_config

    with open(file_name,"r") as f:
        config_data = json.load(f)
        return config_data

def save_config(config_data):
    with open(file_name,"w") as f:
        f.write(json.dump(config_data))

def set_budget(amount):
    if amount <= 0:
        return False
    config = load_config()
    config["monthly_budget"] = amount
    save_config(config)

def get_budget():
    budget = load_config()
    return budget.get("monthly_budget",0)
