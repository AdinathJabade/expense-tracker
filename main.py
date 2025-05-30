from datetime import datetime
from utils import load_expenses, save_expenses

def add_expense():
    """Add a new expense entry."""
    category = input("Enter expense category (e.g., Food, Rent): ")
    
    # Validate amount input
    while True:
        try:
            amount = float(input("Enter amount spent: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if date_str == "":
        date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        # Validate date format
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Using today's date instead.")
            date_str = datetime.now().strftime("%Y-%m-%d")

    note = input("Any note? (optional): ")

    expense = {
        "category": category,
        "amount": amount,
        "date": date_str,
        "note": note
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def list_expenses():
    """List all recorded expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nAll Expenses:")
    print("{:<12} {:<10} {:<12} {}".format("Date", "Category", "Amount", "Note"))
    print("-"*50)
    for exp in expenses:
        print("{:<12} {:<10} ${:<11.2f} {}".format(exp["date"], exp["category"], exp["amount"], exp["note"]))

def main():
    print("=== Expense Tracker ===")
    while True:
        print("\nOptions:")
        print("1. Add expense")
        print("2. List all expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
