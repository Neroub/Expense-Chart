from datetime import datetime


class Expense:
    def __init__(self, amount: float, category: str, date: str):
        self.amount = amount
        self.category = category.strip().lower()
        self.date = datetime.strptime(date, "%Y-%m-%d").date()

    def to_dict(self) -> dict:
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%Y-%m-%d"),
        }