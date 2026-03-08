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
    month = input("Enter month (in numbers): ").strip()
    year = input("Enter year: ").strip()
    return budgets.Budgets(month, year)

def main():
    display.appGreeting()

    if storage.data_exists():
        pass
        data = storage.load()
        currBudget = budgets.Budgets.from_dict(data)
        print(f"Welcome back! Loaded budget for {currBudget.get_month()} {currBudget.get_year()}")
    else:
        print("No budget found. Let's create a new one.")
        currBudget = create_new_budget()

    while True:
        display.setGreen()
        print("\n--- MENU ---")
        print("1. View summary")
        print("2. View income")
        print("3. View expenses")
        print("4. Add income")
        print("5. Add expense")
        print("6. Manage grocery list")
        print("7. Save & exit")

        choice = input("Choose an option: ").strip()
        
        match choice:
            case "1":
                display.display_budget(currBudget)
            case "2":
                currBudget.get_income_list()
            case "3":
                currBudget.get_expense_list()
            case "4": #add income
                income.prompt_income(currBudget)
                # currBudget.add_income(source=input("where from? "),amount=int( input("how much?")),date=input("what day per month does it come? leave if once:"))
                  # to be implemented
            case "5": # add expense
                currBudget.add_expense(name=input("what was the expense?"), amount=int(input("how much?")), category=input("what category?"), date=input("when? leave if once"))
                  # to be implemented
            case "6": # merge list with expense
                
                pass  # to be implemented
            case "7":
                
                storage.save(currBudget.to_dict())
                print("Budget saved! Goodbye.")
                break
            case _:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
