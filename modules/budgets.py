import datetime
class Budgets():
    def __init__(self, month: int, year: int):
        
        self.month = month
        self.year = year
        self.income_list = []    
        self.expense_list = []      
        self.grocery_list = []   
           
    def total_income(self):
        return sum(entry["amount"] for entry in self.income_list )
    def total_expenses(self):
        return sum(entry["amount"] for entry in self.expense_list)
    def balance(self):
        return(self.total_income() - self.total_expenses())

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def get_income_list(self):
        for entry in self.income_list:
            print(entry)

    def get_expense_list(self):
        for entry in self.expense_list:
            print(entry)

    def get_grocery_list(self):
        for entry in self.grocery_list:
            print(entry)



    def add_income(self, source, amount,date:datetime.date):
        '''
        for the date object remember that income is depending on the day that income arrives 
        '''
        self.income_list.append({"source":source,"amount":amount,"date":date})
        
        
    def add_expense(self, name, amount, category, date:datetime.date):
        '''
        for the date object remember that income is depending on the day that expense arrives 
        '''
        self.expense_list.append({"name":name,"amount":amount,"category":category, "date":date})
        
    def get_expenses_by_category(self, category):
        # get a filtered list thats filtered by expenses
        return [entry for entry in self.expense_list if entry["category"] == category]


    
    def add_grocery_item(self, name, estimated_cost):
        self.grocery_list.append({"item-name":name,"estimated-cost":estimated_cost})
    def remove_grochery_item(self, name):
        self.grocery_list = [lis for lis in self.grocery_list if lis.get("item-name") != name]
    def grochery_total(self):
        return [entry["estimated-cost"] for entry in self.grocery_list]
        
    
    
    def get_summary(self):
        return {
            "month": self.month,
            "year": self.year,
            "total_income": self.total_income(),
            "total_expenses": self.total_expenses(),
            "balance": self.balance(),
            "income_list": self.income_list,
            "expense_list": self.expense_list,
            "grocery_list": self.grocery_list,
        }
    
    def to_dict(self):
        return {
            "month": self.month,
            "year": self.year,
            "income_list": [{**entry, "date": entry["date"].isoformat()} for entry in self.income_list],
            "expense_list": [{**entry, "date": entry["date"].isoformat()} for entry in self.expense_list],
            "grocery_list": self.grocery_list,
        }
        
    @classmethod
    def from_dict(cls, data):
        budget = cls(data["month"], data["year"])
        budget.income_list = [{**entry, "date": datetime.date.fromisoformat(entry["date"])} for entry in data["income_list"]]
        budget.expense_list = [{**entry, "date": datetime.date.fromisoformat(entry["date"])} for entry in data["expense_list"]]
        budget.grocery_list = data["grocery_list"]
        return budget
    
    
def quickTestForIncome():
        '''test total income and add income'''
        test_budget = Budgets(1, 2024)
        test_budget.add_income("Salary", 5000, datetime.date(2024,1,1))
        test_budget.add_income("Freelance", 2000, datetime.date(2024,1,15))
        test_budget.add_expense("big money",450,"bills",datetime.date(2024,1,30))
        test_budget.add_grocery_item("food",23)
        test_budget.add_grocery_item("food2",30)
        print(next((i for i in test_budget.grocery_list if i["item-name"] == "food2"), None))
        
        assert test_budget.total_income() == 7000
        print(test_budget.total_income())
        print("Income test passed!")
        print(test_budget.get_summary())
# quickTestForIncome()