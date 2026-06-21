import matplotlib.pyplot as plt


def chart_builder(expenses):
    if not expenses:
        print("Нет данных для построения графика.")
        return

    category_totals = {}
    for exp in expenses:
        category_totals[exp.category] = category_totals.get(exp.category, 0) + exp.amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title("Расходы по категориям")
    plt.axis('equal')
    plt.show()
