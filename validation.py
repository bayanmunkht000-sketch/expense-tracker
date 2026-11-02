from datetime import datetime

def normalize_date(date_text):
    try:
        date = datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        try:
            date = datetime.strptime(date_text, "%Y/%m/%d")
        except ValueError:
            return None

    return date.strftime("%Y-%m-%d")


def positive_number(prompt):
    while True:
        try:
            positive = float(input(prompt))
            if positive <= 0:
                print("Negative number not accepted.")
                continue
            return positive
        except ValueError:
            print("Please enter a positive number.")