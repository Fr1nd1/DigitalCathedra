money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0

while money_capital >= 0:
    # расходы на текущий месяц
    spend_after_increase = spend * (1 + increase) ** month
    # уменьшаем финансовую подушку безопасности
    money_capital += salary - spend_after_increase
    if money_capital < 0:
        break

    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
