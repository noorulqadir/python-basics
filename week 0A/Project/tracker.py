FILENAME = "expenses.txt"


def get_amount():
    # Keep asking until the user enters a positive number.
    # (Use the version from Part 4.)
    while True:
        try:
            amount = float(input("Enter a number: "))
            if amount <= 0:
                print("Amount must be positive")
                continue
            return amount
        except ValueError:
            print("Please Enter a Valid number.")


def add_expense():
    amount = get_amount()
    category = input("Category: ").strip().lower()
    description = input("Description: ").strip()
    # Append one line "amount|category|description\n" to FILENAME
    with open(FILENAME, "a") as file:
        file.write(f"{amount}|{category}|{description}\n")
    print("Expense saved.")


def load_expenses():
    # Return a list of dictionaries like
    # {"amount": 12.5, "category": "food", "description": "lunch"}
    # If the file doesn't exist, return an empty list.
    # For each line: strip it, split on "|", convert amount with float().
    expenses = []
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                amount = float(parts[0])
                category = parts[1]
                description = parts[2]
                expence = {
                    "amount" : amount,
                    "description" : description,
                    "category": category
                }
                expenses.append(expence)
    except FileNotFoundError:
        return []
    return expenses



def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['amount']:.2f} | {expense['category']} | {expense['description']}")


def total_expenses():
    expenses = load_expenses()
    # Add up every expense["amount"] using the accumulator pattern.
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total spent: {total:.2f}")
    return total


def totals_by_category():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return
    totals = {}
    for expense in expenses:
        category = expense["category"]
        # Day 4 pattern: totals[category] = totals.get(category, 0) + amount
        amount = expense["amount"]
        totals[category] = totals.get(category, 0) + amount

    for category, amount in totals.items():
        print(f"{category}: {amount:.2f}")

# def delete_expense():
#     expenses = load_expenses()
#     if not expenses:
#         print("No expense to delete.")
#         return
    



def main():
    while True:
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. View total")
        print("4. View totals by category")
        print("5. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            totals_by_category()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()