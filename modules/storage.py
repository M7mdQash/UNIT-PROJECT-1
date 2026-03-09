import json
import os

DATA_FILE = "data/budget_data.json"

def _load_all():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def _save_all(data):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def list_budgets():
    return list(_load_all().keys())

def save(budget_dict):
    key = f"{budget_dict['year']}-{budget_dict['month']}"
    all_data = _load_all()
    all_data[key] = budget_dict
    _save_all(all_data)

def load(key):
    return _load_all()[key]

def data_exists():
    return os.path.exists(DATA_FILE) and bool(_load_all())
