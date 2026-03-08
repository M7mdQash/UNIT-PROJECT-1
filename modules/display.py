from colorama import *
from art import *
import calendar

def appGreeting():
    artPhrase3 = text2art("budgeting", font="sub-zero", chr_ignore=True)
    print(Fore.BLUE + artPhrase3)
    print("welcome to the budgeting app")
    Fore.RESET

def setGreen():
    print(Fore.GREEN)

def display_budget(budget):
    month_name = budget.get_month()
    year = budget.get_year()

    print(Fore.CYAN + f"\n{'='*40}")
    print(f"  Budget: month of {month_name} year of {year}")
    print(f"{'='*40}" + Style.RESET_ALL)

    # Income
    print(Fore.GREEN + "\n  Income:")
    if budget.income_list:
        for entry in budget.income_list:
            print(f"    [{entry['date']}] {entry['source']}: ${entry['amount']:.2f}")
    else:
        print("    No income recorded.")
    print(f"  Total Income: ${budget.total_income():.2f}" + Style.RESET_ALL)

    # Expenses
    print(Fore.RED + "\n  Expenses:")
    if budget.expense_list:
        for entry in budget.expense_list:
            print(f"    [{entry['date']}] {entry['name']} ({entry['category']}): ${entry['amount']:.2f}")
    else:
        print("    No expenses recorded.")
    print(f"  Total Expenses: ${budget.total_expenses():.2f}" + Style.RESET_ALL)

    # Groceries
    print(Fore.YELLOW + "\n  Grocery List:")
    if budget.grocery_list:
        for item in budget.grocery_list:
            print(f"    {item['item-name']}: ${item['estimated-cost']:.2f}")
    else:
        print("    No grocery items.")
    print(Style.RESET_ALL)

    # Balance
    balance = budget.balance()
    color = Fore.GREEN if balance >= 0 else Fore.RED
    print(color + f"  Balance: ${balance:.2f}")
    print(Fore.CYAN + f"{'='*40}\n" + Style.RESET_ALL)