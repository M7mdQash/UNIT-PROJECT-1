DEFAULT_CATEGORIES = ["daily", "bills", "transport", "food", "other", "grocheries"]

def get_categories():
    return DEFAULT_CATEGORIES

def validate_categories(category):
    #we just check if the category is already in, its an if statment so we dont dupicate 
    if category not in DEFAULT_CATEGORIES:
        return False
    else:
        return True

def prompt_category():
    print(f"current categories of expenses are: {DEFAULT_CATEGORIES}")
    if input("would you like to enter a new category? (y/n)").strip().lower() == "y" or "yes":
        return input("please input the new category")
    
    else:
        return False