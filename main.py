def add_expense():
    category = input("Enter expense category: ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    with open("expense_tracker.txt", "a") as file:
        file.write(category + "," + str(amount) + "\n")


def show_expenses():
    total = 0

    with open("expense_tracker.txt", "r") as file:
        content = file.read()

    lines = content.split("\n")

    for line in lines:
        if line.strip() == "":
            continue

        pieces = line.split(",")
        category = pieces[0]
        amount = float(pieces[1])

        total += amount
        print(category, amount)

    print("Your Total is:", total)

def delete_expense():
    with open("expense_tracker.txt", "r") as file:
        content = file.read()

    lines = content.splitlines()

    for index, line in enumerate(lines, start=1):
        if line.strip() == "":
            continue

        print(index, line)
    while True:
        try:
            choice = int(input("Which expense do you want to delete? "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if 1 <= choice <= len(lines):
            delete_index = choice - 1
            lines.pop(delete_index)
            break
        else:
            print("Expense does not exist.")

    with open("expense_tracker.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")



def main():
    while True:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Welcome to the Baynaa's Expense Tracker!")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("What would you like to do?")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Delete expense")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("please enter a valid number.")
            continue
        if choice == 1:
            add_expense()
        elif choice == 2:
            show_expenses()
        elif choice == 3:
            delete_expense()
        elif choice == 4:
            break
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()