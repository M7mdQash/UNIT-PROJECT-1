def prompt_import_income(budget):
    from modules import storage
    curr_key = f"{budget.get_year()}-{budget.get_month()}"
    options = [k for k in storage.list_budgets() if k != curr_key]
    if not options:
        print("No other budgets available to import from.")
        return
    print("\nSelect budget to import income from:")
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
    count = storage.import_dated_income(options[idx], budget)
    print(f"Imported {count} dated income entries from {options[idx]}.")

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

    day_input = input(f"Enter day (1-28, leave blank for no date): ").strip()
    if not day_input:
        day = None
    else:
        try:
            day = int(day_input)
            if not (1 <= day <= 28):
                raise ValueError
        except ValueError:
            print(f"Invalid day. Must be between 1 and 28.")
            return None

    budget.add_income(source, amount, day)
    print(f"Income added: {source} - {amount}" + (f" on day {day}" if day else ""))
