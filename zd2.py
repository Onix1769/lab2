salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен


def calculate_safety_buffer(salary, initial_spend, months, increase):
    total_needed = 0  # Общая сумма, необходимая для покрытия расходов
    spend = initial_spend  # Начальные расходы

    for month in range(months):
        # В этом месяце зарплата покрывает часть расходов
        if salary < spend:
            # Если зарплаты не хватает, добавляем недостающую сумму к общей
            total_needed += spend - salary

        # Увеличиваем расходы на процент роста цен
        spend *= (1 + increase)

    return total_needed


def main():
    salary = 5000  # Ежемесячная зарплата
    initial_spend = 6000  # Траты за первый месяц
    months = 10  # Количество месяцев, которое планируется протянуть без долгов
    increase = 0.05  # Ежемесячный рост цен

    # Рассчитываем необходимую подушку безопасности
    safety_buffer = calculate_safety_buffer(salary, initial_spend, months, increase)

    # Округляем до целого числа
    safety_buffer = round(safety_buffer)

    print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {safety_buffer} рублей")

if __name__ == "__main__":
    main()