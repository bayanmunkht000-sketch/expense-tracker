import json

def load_expenses():
    try:
        with open('expenses.json', "r") as file:
            expenses = json.load(file)
            return expenses
    except FileNotFoundError:
        expenses = []
        return expenses
    except json.JSONDecodeError:
        print("Expense data is corrupted.")
        return []


def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)