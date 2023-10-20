money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
total_amount = money_capital - spend

if total_amount > 0:
    total_amount += salary
    month += 1
    spend_after_increase = spend * (1 + increase)

    while total_amount - spend_after_increase > 0:
        month += 1
        total_amount -= spend_after_increase
        total_amount += salary
        spend_after_increase = spend_after_increase * (1 + increase)

    # Последний месяц, когда останется хоть какая-то подушка безопасности. К 1 числу следующего месяца она полностью иссякнет
    month += 1
    print("Количество месяцев, которое можно протянуть без долгов:", month)
elif total_amount == 0:
    month += 1
    print("Количество месяцев, которое можно протянуть без долгов:", month)
else:
    print("Количество месяцев, которое можно протянуть без долгов:", month)