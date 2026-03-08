import json
import os

DATA_FILE = "data/budget_data.json"

def save(budget_dict):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(budget_dict, f, indent=4)

def load():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def data_exists():
    return os.path.exists(DATA_FILE)
