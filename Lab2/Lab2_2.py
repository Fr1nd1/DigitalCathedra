salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 1000
spend_after_increase = spend

for month in range(2, months + 1):
    spend_after_increase *= (1 + increase)
    remaining_balance = salary - spend_after_increase
    if remaining_balance < 0:
        money_capital -= remaining_balance

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
