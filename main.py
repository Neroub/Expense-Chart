import datetime
from expense import Expense
from expense_manager import ExpenseManager
from build_chart import chart_builder


class ConsoleUI:
    def __init__(self):
        self.manager = ExpenseManager()

    def get_valid_amount(self):
        while True:
            try:
                amount = float(input("Введите сумму расхода: "))
                if amount <= 0:
                    print("Ошибка: Сумма должна быть строго больше нуля.")
                    continue
                return amount
            except ValueError:
                print("Ошибка: Введите корректное число.")

    def get_valid_date(self, prompt):
        while True:
            date_str = input(prompt)
            try:
                return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                print("Ошибка: Неверный формат даты. Используйте ГГГГ-ММ-ДД (например, 2026-06-21).")

    def main(self):
        while True:
            print("\n--- Expense Chart Menu ---")
            print("1. Добавить расход")
            print("2. Показать все расходы")
            print("3. Удалить расход")
            print("4. Фильтрация и статистика")
            print("5. Построить график расходов")
            print("6. Выход")

            choice = input("Выберите действие: ").strip()

            if choice == "1":
                amount = self.get_valid_amount()
                category = input("Введите категорию: ")
                date_obj = self.get_valid_date("Введите дату (ГГГГ-ММ-ДД): ")
                expense = Expense(amount, category, date_obj.strftime("%Y-%m-%d"))
                self.manager.add_expense(expense)
                print("Расход успешно добавлен!")

            elif choice == "2":
                self.manager.view_expenses()

            elif choice == "3":
                self.manager.view_expenses()
                try:
                    idx = int(input("Введите индекс для удаления: "))
                    if self.manager.remove_expense(idx):
                        print("Запись удалена.")
                    else:
                        print("Неверный индекс.")
                except ValueError:
                    print("Ошибка ввода.")

            elif choice == "4":
                print("Оставьте поле пустым, если фильтр не нужен.")
                cat = input("Категория для фильтра: ").strip() or None

                start_str = input("Начальная дата (ГГГГ-ММ-ДД) или Enter: ").strip()
                start_date = datetime.datetime.strptime(start_str, "%Y-%m-%d").date() if start_str else None

                end_str = input("Конечная дата (ГГГГ-ММ-ДД) или Enter: ").strip()
                end_date = datetime.datetime.strptime(end_str, "%Y-%m-%d").date() if end_str else None

                filtered = self.manager.expenses_filter(cat, start_date, end_date)
                print("\n--- Результаты фильтрации ---")
                for exp in filtered:
                    print(exp)
                total = self.manager.expenses_sum(filtered)
                print(f"Общая сумма за период: {total:.2f} руб.")

            elif choice == "5":
                chart_builder(self.manager.expenses)

            elif choice == "6":
                print("До свидания!")
                break
            else:
                print("Неверный ввод.")


if __name__ == "__main__":
    app = ConsoleUI()
    app.main()