from storage import load_expenses

from expenses import (
    add_expense,
    show_expenses,
    delete_expense,
    edit_expense,
    search_by_category,
    search_by_amount,
    search_by_date,
    search_by_name
)

from analytics import (
    show_statistics,
    spending_by_category,
    monthly_spending,
    daily_spending
)

from validation import normalize_date

def main():
    expenses = load_expenses()
    while True:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Welcome to the Baynaa's Expense Tracker!")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("What would you like to do?")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Delete expense")
        print("4. Edit expense")
        print("5. Search by category")
        print("6. Search by amount")
        print("7. Search by date")
        print("8. Search by name")
        print("9. Show statistics")
        print("10. Spending by category")
        print("11. Search by Month")
        print("12. Daily Spending")
        print("14. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("please enter a valid number.")
            continue
        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            show_expenses(expenses)
        elif choice == 3:
            delete_expense(expenses)
        elif choice == 4:
            edit_expense(expenses)
        elif choice == 5:
            search_by_category(expenses)
        elif choice == 6:
            search_by_amount(expenses)
        elif choice == 7:
            search_by_date(expenses)
        elif choice == 8:
            search_by_name(expenses)
        elif choice == 9:
            show_statistics(expenses)
        elif choice == 10:
            spending_by_category(expenses)
        elif choice == 11:
            monthly_spending(expenses)
        elif choice == 12:
            daily_spending(expenses)
        elif choice == 13:
            break
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()