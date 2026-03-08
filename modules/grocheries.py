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
    #this one does it loop like for all the grocheries
    list = budget.grocery_list
    for items in list:
        pass