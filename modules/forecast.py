import datetime
"""
Budget Forecast Report Module

This module generates a comprehensive financial forecast report based on a list of budget objects.
It analyzes income, expenses, and planned purchases across multiple budget periods and displays
a detailed breakdown with trend analysis.

Key Features:
    - Displays income entries (dated and one-time)
    - Displays expense entries (dated and one-time)
    - Shows planned grocery/purchase list items
    - Calculates monthly balances
    - Provides trend analysis comparing periods
    - Color-coded output for better readability (using colorama)
    - Validates date ranges across budgets with warnings

Functions:
    run(budgets_list): Main function that generates and prints the forecast report

Helper Functions:
    _budget_date(budget): Extracts date from a budget object
    _check_date_range(budgets_list): Validates that budgets span within 3 years
    _dated(entries): Filters entries with assigned dates
    _undated(entries): Filters entries without assigned dates
    _total(entries, key): Sums a specific key value from entries
    _print_income_entries(entries, label): Prints formatted income entries
    _print_expense_entries(entries, label): Prints formatted expense entries

Constants:
    DIVIDER: Visual separator for major sections (50 chars)
    SECTION: Visual separator for subsections (40 chars)
    MAX_GAP_DAYS: Maximum allowed date range between budgets (3 years in days)

Output Format:
    - Budget details organized by month/year
    - Income section with regular and one-time sources
    - Expense section with regular and one-time costs
    - Grocery list with estimated costs
    - Monthly balance (green if positive, red if negative)
    - Trend summary showing balance changes across periods
"""
import calendar
from colorama import Fore, Style

DIVIDER = "=" * 50
SECTION  = "-" * 40
MAX_GAP_DAYS = 365 * 3


def _budget_date(budget):
    return datetime.date(int(budget.get_year()), int(budget.get_month()), 1)


def _check_date_range(budgets_list):
    dates = sorted(_budget_date(b) for b in budgets_list)
    return (dates[-1] - dates[0]).days <= MAX_GAP_DAYS


def _dated(entries):
    return [e for e in entries if e.get("date") is not None]


def _undated(entries):
    return [e for e in entries if e.get("date") is None]


def _total(entries, key="amount"):
    return sum(e[key] for e in entries)


def _print_income_entries(entries, label):
    print(f"  {label}:")
    if entries:
        for e in entries:
            date_str = f"[{e['date']}] " if e.get("date") else ""
            print(f"    {date_str}{e['source']}: ${e['amount']:.2f}")
    else:
        print("    None")


def _print_expense_entries(entries, label):
    print(f"  {label}:")
    if entries:
        for e in entries:
            date_str = f"[{e['date']}] " if e.get("date") else ""
            print(f"    {date_str}{e['name']} ({e['category']}): ${e['amount']:.2f}")
    else:
        print("    None")


def run(budgets_list):
    if not budgets_list:
        print("No budgets to forecast.")
        return

    budgets_list = sorted(budgets_list, key=_budget_date)

    if not _check_date_range(budgets_list):
        print(Fore.YELLOW + f"Warning: budgets span more than 3 years — comparison may be less meaningful." + Style.RESET_ALL)

    print(Fore.CYAN + f"\n{DIVIDER}")
    print("  BUDGET FORECAST REPORT")
    print(f"{DIVIDER}" + Style.RESET_ALL)

    balances = []

    for budget in budgets_list:
        month_name = calendar.month_name[int(budget.get_month())]
        year = budget.get_year()

        dated_inc   = _dated(budget.income_list)
        sudden_inc  = _undated(budget.income_list)
        dated_exp   = _dated(budget.expense_list)
        sudden_exp  = _undated(budget.expense_list)
        grocery     = budget.grocery_list

        total_dated_inc   = _total(dated_inc)
        total_sudden_inc  = _total(sudden_inc)
        total_dated_exp   = _total(dated_exp)
        total_sudden_exp  = _total(sudden_exp)
        total_grocery     = sum(item["estimated-cost"] for item in grocery)
        total_income      = total_dated_inc + total_sudden_inc
        total_expenses    = total_dated_exp + total_sudden_exp
        balance           = total_income - total_expenses

        balances.append((f"{month_name} {year}", balance))

        # ── Header ──────────────────────────────────────────
        print(Fore.CYAN + f"\n  {month_name} {year}" + Style.RESET_ALL)
        print(SECTION)

        # ── Income ──────────────────────────────────────────
        print(Fore.GREEN)
        _print_income_entries(dated_inc,  "Regular income (dated)")
        _print_income_entries(sudden_inc, "One-time income (no date)")
        print(f"  Total income: ${total_income:.2f}  "
              f"(regular: ${total_dated_inc:.2f}  |  one-time: ${total_sudden_inc:.2f})")
        print(Style.RESET_ALL, end="")

        # ── Expenses ─────────────────────────────────────────
        print(Fore.RED)
        _print_expense_entries(dated_exp,  "Regular expenses (dated)")
        _print_expense_entries(sudden_exp, "One-time expenses (no date)")
        print(f"  Total expenses: ${total_expenses:.2f}  "
              f"(regular: ${total_dated_exp:.2f}  |  one-time: ${total_sudden_exp:.2f})")
        print(Style.RESET_ALL, end="")

        # ── Purchases list ───────────────────────────────────
        print(Fore.YELLOW + "  Planned purchases (grocery list):")
        if grocery:
            for item in grocery:
                print(f"    {item['item-name']}: ${item['estimated-cost']:.2f}")
            print(f"  Grocery total: ${total_grocery:.2f}")
        else:
            print("    None")
        print(Style.RESET_ALL, end="")

        # ── Balance ──────────────────────────────────────────
        bal_color = Fore.GREEN if balance >= 0 else Fore.RED
        print(bal_color + f"  Balance: ${balance:.2f}" + Style.RESET_ALL)

    # ── Trend summary ────────────────────────────────────────
    if len(balances) > 1:
        print(Fore.CYAN + f"\n{DIVIDER}")
        print("  TREND SUMMARY")
        print(f"{DIVIDER}" + Style.RESET_ALL)

        for i, (label, bal) in enumerate(balances):
            bal_color = Fore.GREEN if bal >= 0 else Fore.RED
            if i > 0:
                diff = bal - balances[i - 1][1]
                sign = "+" if diff >= 0 else ""
                diff_color = Fore.GREEN if diff >= 0 else Fore.RED
                diff_str = diff_color + f"  ({sign}{diff:.2f} vs previous)" + Style.RESET_ALL
            else:
                diff_str = ""
            print(bal_color + f"  {label}: ${bal:.2f}" + Style.RESET_ALL + diff_str)

        overall = balances[-1][1] - balances[0][1]
        sign = "+" if overall >= 0 else ""
        overall_color = Fore.GREEN if overall >= 0 else Fore.RED
        print(overall_color + f"\n  Overall change across all periods: {sign}${overall:.2f}" + Style.RESET_ALL)

    print(Fore.CYAN + f"\n{DIVIDER}\n" + Style.RESET_ALL)
