import json
import os
import datetime

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

def delete(key):
    all_data = _load_all()
    if key in all_data:
        del all_data[key]
        _save_all(all_data)
        return True
    return False

def data_exists():
    return os.path.exists(DATA_FILE) and bool(_load_all())

def import_dated_income(source_key, target_budget):
    data = load(source_key)
    imported = 0
    for entry in data.get("income_list", []):
        if entry.get("date"):
            date_obj = datetime.date(*[int(p) for p in entry["date"].split("-")])
            target_budget.income_list.append({**entry, "date": date_obj})
            imported += 1
    return imported

def import_dated_expenses(source_key, target_budget):
    data = load(source_key)
    imported = 0
    for entry in data.get("expense_list", []):
        if entry.get("date"):
            date_obj = datetime.date(*[int(p) for p in entry["date"].split("-")])
            target_budget.expense_list.append({**entry, "date": date_obj})
            imported += 1
    return imported
