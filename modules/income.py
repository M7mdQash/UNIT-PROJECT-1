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
