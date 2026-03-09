DEFAULT_CATEGORIES = ["daily", "bills", "transport", "food", "other", "grocheries"]

def prompt_import_expenses(budget):
    from modules import storage
    curr_key = f"{budget.get_year()}-{budget.get_month()}"
    options = [k for k in storage.list_budgets() if k != curr_key]
    if not options:
        print("No other budgets available to import from.")
        return
    print("\nSelect budget to import expenses from:")
    for i, key in enumerate(options, 1):
        print(f"  {i}. {key}")
    choice = input("Choose an option: ").strip()
    try:
        idx = int(choice) - 1
        if not (0 <= idx < len(options)):
            print("Invalid option.")
            return
    except ValueError:
        print("Invalid input.")
        return
    count = storage.import_dated_expenses(options[idx], budget)
    print(f"Imported {count} dated expense entries from {options[idx]}.")

def get_categories():
    return DEFAULT_CATEGORIES

def sync_categories_from_budget(budget):
    for entry in budget.expense_list:
        cat = entry.get("category")
        if cat and cat not in DEFAULT_CATEGORIES:
            #check if empty and if not in list first
            DEFAULT_CATEGORIES.append(cat)

def add_category(name):
    if name in DEFAULT_CATEGORIES:
        print(f"Category '{name}' already exists.")
    else:
        DEFAULT_CATEGORIES.append(name)
        print(f"Category '{name}' added.")

# def validate_categories(category):
#     #we just check if the category is already in, its an if statment so we dont dupicate 
#     if category not in DEFAULT_CATEGORIES:
#         return False
#     else:
#         return True

# def prompt_category():
#     print(f"current categories of expenses are: {DEFAULT_CATEGORIES}")
#     if input("would you like to enter a new category? (y/n)").strip().lower() == "y" or "yes":
#         return input("please input the new category")
    
#     else:
#         return False