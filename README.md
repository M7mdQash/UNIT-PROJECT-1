# UNIT-PROJECT-1


## My Project :  A personal budget tracker :

#### Overview : An interactive Command line budget tracker programm that lets you set your budget, income, expenses and view the summary and forecast of every month for you to evaluate your budget

### Features
- add monthly income/any source of income . 
- View the current budget, its expenses and its income
- add expenses and be able to filter them via category (daily expense, bills, transport, etc)
- Get forecast for this month expenses and the next.
- create a list of purcahses to help you figure out if your spendature is recurring or not

### Project Structure
```
UNIT-PROJECT-1/
├── main.py               # Entry point — runs the CLI app
├── requirements.txt      # Project dependencies
├── data/
│   └── budget_data.json  # Saved budget data (auto-generated)
└── modules/
    ├── budgets.py        # Budget class and core logic
    ├── expenses.py       # Expense management and categories
    ├── income.py         # Income management
    ├── forecast.py       # Spending forecast and savings target
    ├── grocheries.py     # Purchases/grocery list management
    ├── display.py        # CLI display helpers (colors, formatting)
    └── storage.py        # JSON load/save/delete operations
```

###  User Stories
#### a users regular usage of the programm should be like so:
1 load previous budget data or create new one
2 view budget, its constraints, expenses and income
3 take notes on budget and expenses
4 view the forecast of spending
5 add expenses or income to budget
6 save data to be loaded again


#### Usage :
##### to use this project do the following
```
 1. Create a virtual environment
python -m venv venv

# 2. Activate it
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
python main.py
```
- the project uses the colerama and art libraries so make sure they are included when you run the project

### Main Menu Reference

| Option | Description |
|--------|-------------|
| 1. Summary | View total income, expenses, and balance |
| 2. Manage income | Add, view, remove income or import from another month |
| 3. Manage expenses | Add, view, remove categorized expenses or import from another month |
| 4. Purchases list | Manage a grocery list and apply it to the budget |
| 5. Forecast | View projected spending across all saved budgets |
| 6. Set savings target | Enter a target and see how long it will take to reach it |
| 7. Switch budget | Save current budget and go back to budget selection |
| 8. Save and exit | Save and quit the app |

### user instructions:
budgets uses a json file to store user info, playing with this file may alter the way the programm functions

after each session remember to save and exit as leaving without saving will not save the data onto the json



