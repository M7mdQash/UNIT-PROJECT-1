from datetime import datetime


def applyGrocheriesToBudget(budget, itemName:str):
    entry = next((i for i in budget.grocery_list if i["item-name"] == itemName), None)
    if entry is None:
        raise Exception("item was not found in list, please add it first")
    else:
        try:
            budget.add_expense(itemName, entry["estimated-cost"], "grocheries", datetime.today().date())
        except Exception as e:
            print("error with adding grocheries", e)
            
def applyAllGrocheriesToBudget(budget):
    total = sum(item["estimated-cost"] for item in budget.grocery_list)
    try:
        budget.add_expense("monthly purchases", total, "grocheries" )
    except Exception as e:
        print("error with adding grocheries", e)

def resetGroceryList(budget):
    budget.grocery_list = []