class FinancialTracker:
    def __init__(self):
        self.income = []
        self.expenses = []

    def add_income(self, source, amount):
        self.income.append((source, amount))

    def add_expense(self, category, amount):
        self.expenses.append((category, amount))

    def display_financial_summary(self):
        total_income = sum(amount for _, amount in self.income)
        total_expenses = sum(amount for _, amount in self.expenses)
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Net Savings: {total_income - total_expenses}")
if __name__ == "__main__":
    tracker = FinancialTracker()
    tracker.add_income("Job", 3300)
    tracker.add_expense("Rent", 1500)
    tracker.add_expense("Groceries", 1000)
    tracker.display_financial_summary()
