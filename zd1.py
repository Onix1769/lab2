money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


def calculate_months_without_debt(money_capital, salary, initial_spend, increase):
    months = 0  # Счетчик месяцев
    spend = initial_spend  # Начальные расходы

    # Цикл, пока есть возможность покрывать расходы
    while True:
        # Рассчитываем текущий бюджет
        current_budget = salary + money_capital

        # Проверяем, хватает ли бюджета на текущие расходы
        if current_budget < spend:
            break  # Если нет, то выходим из цикла

        # Увеличиваем счетчик месяцев
        months += 1

        # Уменьшаем капитал на текущие расходы, если зарплаты не хватает
        money_capital -= max(0, spend - salary)

        # Увеличиваем траты на рост цен
        spend *= (1 + increase)

    return months


def main():
    money_capital = 20000  # Подушка безопасности
    salary = 5000  # Ежемесячная зарплата
    initial_spend = 6000  # Траты за первый месяц
    increase = 0.05  # Ежемесячный рост цен

    # Рассчитываем количество месяцев, которые можно протянуть без долгов
    months = calculate_months_without_debt(money_capital, salary, initial_spend, increase)

    print(f"Количество месяцев, которое можно протянуть без долгов: {months}")


if __name__ == "__main__":
    main()
