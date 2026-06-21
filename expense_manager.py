import json
from expense import Expense


class ExpenseManager:
    def __init__(self, file_name="expenses.json"):
        self.file_name = file_name
        self.expenses = []
        self.load_json()

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
        self.save_json()

    def remove_expense(self, index: int):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            self.save_json()

    def view_expenses(self):
        for i, expense in enumerate(self.expenses):
            print(f"{i}. {expense.amount}.{expense.category}.{expense.date}")

    def expenses_sum(self, sum_list):
        return sum(e.amount for e in sum_list)

    def expenses_filter(self, category=None, start_date=None, end_date=None):
        filtered = self.expenses
        if category:
            filtered = [e for e in filtered if e.category.lower() == category.lower()]
        if start_date:
            filtered = [e for e in filtered if e.date >= start_date]
        if end_date:
            filtered = [e for e in filtered if e.date <= end_date]
        return filtered

    def save_json(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in self.expenses], f, ensure_ascii=False, indent=4)

    def load_json(self):
        with open(self.file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.expenses = []
            for expense in data:
                self.expenses.append(Expense(expense["amount"], expense["category"], expense["date"]))
