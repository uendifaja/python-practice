from datetime import datetime
from tabulate import tabulate 

def show_menu():
    print("\n--- 💸 Expense Tracker ---")
    print("1. ➕ Add expense")
    print("2. 📄 View expenses")
    print("3. 📊 View summary")
    print("4. 🗓 Monthly summary")
    print("5. 🚪 Exit")

def add_expense():
    amount = input("Enter € amount: ")
    category = input("Enter category (Food, Rent, Shopping, etc.): ")
    note = input("Add a note (optional): ")

    date = datetime.now().strftime("%Y-%m-%d")  # as 2025-02-15

    with open("expenses.csv", "a") as file:
        file.write(f"{date},{amount},{category},{note}\n")

    print("Expense added successfully!")

def view_expenses():
    print("\n--- Your Expenses ---")
    try:
        with open("expenses.csv", "r") as file:
            lines = file.readlines()

            if not lines:
                print("No expenses recorded yet.")
                return

            rows = []
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) != 4:
                    continue
                rows.append(parts)

            headers = ["Date", "Amount (€)", "Category", "Note"]
            print(tabulate(rows, headers=headers, tablefmt="github"))

    except FileNotFoundError:
        print("No expenses file found. Add an expense first!")

def view_summary():
    print("\n--- Expense Summary ---")

    try:
        with open("expenses.csv", "r") as file:
            lines = file.readlines()

            if not lines:
                print("No expenses recorded yet.")
                return

            total = 0
            categories = {}

            for line in lines:
                date, amount, category, note = line.strip().split(",")
                amount = float(amount)  # convert to number
                total += amount

                if category not in categories:
                    categories[category] = 0
                categories[category] += amount

            print(f"Total spent: {total}€")

            print("\nSpending by category:")
            for category, amount in categories.items():
                print(f"- {category}: {amount}€")

    except FileNotFoundError:
        print("No expenses file found. Add an expense first!")

def monthly_summary():
    print("\n--- Monthly Summary ---")
    month = input("Enter month (YYYY-MM): ")  # e.g. 2025-02

    total = 0
    category_totals = {}

    try:
        with open("expenses.csv", "r") as file:
            lines = file.readlines()

            if not lines:
                print("No expenses recorded yet.")
                return

            for line in lines:
                date, amount, category, note = line.strip().split(",")

                if date.startswith(month):  # matches YYYY-MM
                    amount = float(amount)
                    total += amount

                    if category not in category_totals:
                        category_totals[category] = 0
                    category_totals[category] += amount

        print(f"\nTotal spent in {month}: {total}€")
        print("\nBreakdown by category:")
        for cat, amt in category_totals.items():
            print(f"- {cat}: {amt}€")

        if total == 0:
            print("No expenses found for this month.")

    except FileNotFoundError:
        print("No expenses file found. Add an expense first!")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
