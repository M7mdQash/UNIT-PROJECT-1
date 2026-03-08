import datetime
import calendar


def prompt_income(budget):
    source = input("Enter income source: ").strip()
    if not source:
        print("Source cannot be empty.")
        return None

    amount_input = input("Enter amount: ").strip()
    try:
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Invalid amount. Must be a positive number.")
        return None

    month = budget.get_month()
    year = budget.get_year()
    # max_day = calendar.monthrange(year, month)[1]

    day_input = input(f"Enter day (1-28): ").strip()
    try:
        day = int(day_input)
        if not (1 <= day <= 28):
            raise ValueError
    except ValueError:
        print(f"Invalid day. Must be between 1 and 28.")
        return None

    date = datetime.date(int(year), int(month), int(day))
    budget.add_income(source, amount, date)
    print(f"Income added: {source} - {amount} on {date}")
