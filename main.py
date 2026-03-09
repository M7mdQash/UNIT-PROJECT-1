'''
this will be the main method
'''

from modules import display
from modules import budgets
from modules import grocheries
from modules import storage
from modules import expenses
from modules import income
import datetime


def create_new_budget():
    try:
        month = int(input("Enter month (1-12): ").strip())
        year = int(input("Enter year: ").strip())
    except ValueError:
        print("Invalid input. Month and year must be numbers.")
        return None
    return budgets.Budgets(month, year)

def pick_budget():
    saved = storage.list_budgets()
    
    print("\nSaved budgets:")
    for i, key in enumerate(saved, 1):
        print(f"  {i}. {key}")
    print(f"  {len(saved) + 1}. Create new budget")

    choice = input("Choose an option: ").strip()
    try:
        idx = int(choice) - 1
    except ValueError:
        print("Invalid input.")
        return None

    if idx == len(saved):
        return create_new_budget()
    elif 0 <= idx < len(saved):
        data = storage.load(saved[idx])
        budget = budgets.Budgets.from_dict(data)
        print(f"Loaded budget for {budget.get_month()}/{budget.get_year()}")
        return budget
    else:
        print("Invalid option.")
        return None

def main():
    display.appGreeting()

    if storage.data_exists():
        currBudget = pick_budget()
    else:
        print("No budgets found. Let's create a new one.")
        currBudget = create_new_budget()

    if currBudget is None:
        print("No budget selected. Exiting.")
        return

    expenses.sync_categories_from_budget(currBudget)

    while True:
        display.setGreen()
        print("\n--- MENU ---")
        print("1. Summary")
        print("2. Manage income")
        print("3. Manage expenses")
        print("4. Purchases list (groceries)")
        print("5. Save and exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                display.display_budget(currBudget)

            case "2":
                while True:
                    print("\n--- INCOME ---")
                    print("1. View income")
                    print("2. Add income")
                    print("3. Remove income")
                    print("4. Back")
                    sub = input("Choose an option: ").strip()
                    if sub == "1":
                        currBudget.get_income_list()
                    elif sub == "2":
                        income.prompt_income(currBudget)
                    elif sub == "3":
                        source = input("Source to remove: ").strip()
                        try:
                            currBudget.remove_income(source)
                            print("Income removed.")
                        except Exception as e:
                            print(f"Error removing income: {e}")
                    elif sub == "4":
                        break
                    else:
                        print("Invalid option.")

            case "3":
                while True:
                    print("\n--- EXPENSES ---")
                    print("1. View expenses")
                    print("2. Add expense")
                    print("3. Remove expense")
                    print("4. View categories")
                    print("5. Add category")
                    print("6. Back")
                    sub = input("Choose an option: ").strip()
                    if sub == "1":
                        currBudget.get_expense_list()
                    elif sub == "2":
                        name = input("Expense name: ").strip()
                        try:
                            amount = float(input("Amount: ").strip())
                        except ValueError:
                            print("Invalid amount.")
                            continue
                        category = input("Category: ").strip()
                        day_input = input("Day (1-28, leave blank for no date): ").strip()
                        day = int(day_input) if day_input else None
                        currBudget.add_expense(name, amount, category, day)
                        print("Expense added.")
                    elif sub == "3":
                        name = input("Expense name to remove: ").strip()
                        try:
                            currBudget.remove_expense(name)
                            print("Expense removed.")
                        except Exception as e:
                            print(f"Error removing expense: {e}")
                    elif sub == "4":
                        print("Categories:", expenses.get_categories())
                    elif sub == "5":
                        new_cat = input("New category name: ").strip()
                        expenses.add_category(new_cat)
                    elif sub == "6":
                        break
                    else:
                        print("Invalid option.")

            case "4":
                while True:
                    print("\n--- PURCHASES ---")
                    print("1. View purchases list")
                    print("2. Add item")
                    print("3. Remove item")
                    print("4. Apply all to budget")
                    print("5. Back")
                    sub = input("Choose an option: ").strip()
                    if sub == "1":
                        currBudget.get_grocery_list()
                    elif sub == "2":
                        item_name = input("Item name: ").strip()
                        try:
                            cost = float(input("Estimated cost: ").strip())
                        except ValueError:
                            print("Invalid cost.")
                            continue
                        currBudget.add_grocery_item(item_name, cost)
                        print("Item added.")
                    elif sub == "3":
                        item_name = input("Item name to remove: ").strip()
                        try:
                            currBudget.remove_grochery_item(item_name)
                            print("Item removed.")
                        except Exception as e:
                            print(f"Error removing item: {e}")
                    elif sub == "4":
                        grocheries.applyAllGrocheriesToBudget(currBudget)
                        grocheries.resetGroceryList(currBudget)
                        print("All items applied to budget and purchases list cleared.")
                    elif sub == "5":
                        break
                    else:
                        print("Invalid option.")

            case "5":
                storage.save(currBudget.to_dict())
                print("Budget saved! Goodbye.")
                break

            case _:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
