"""4. Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами. Клиент банка
делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых)
10000–100000 руб (6 месяцев — 6 % годовых,год — 7 % годовых, 2 года – 6.5 % годовых)
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).

Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада.
Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами
(begin_sum, end_sum, 6, 12, 24).

Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого
срока. В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет по нужной
процентной ставке. Функция возвращает сумму вклада на конец срока. """


def count_deposit(money_sum: int, time_money: int) -> float:
    """

    :param money_sum:
    :param time_money:
    :return:
    """
    deposit_1 = {
        "begin_sum": 1000,
        "end_sum": 10000,
        6: 0.05,
        12: 0.06,
        24: 0.05
    }

    deposit_2 = {
        "begin_sum": 10000,
        "end_sum": 100000,
        6: 0.06,
        12: 0.07,
        24: 0.065
    }

    deposit_3 = {
        "begin_sum": 100000,
        "end_sum": 1000000,
        6: 0.07,
        12: 0.08,
        24: 0.075
    }

    deposits = [
        deposit_1,
        deposit_2,
        deposit_3
    ]

    for deposit in deposits:
        if deposit.get("begin_sum") <= money_sum < deposit.get("end_sum"):
            if time_money <= 12:
                return money_sum + money_sum * deposit.get(time_money) * time_money / 12
            # Сделаем начисление первых процентов за первый год на счёт депозита:
            if time_money == 24:
                money_sum = money_sum + money_sum * deposit.get(time_money)
                return money_sum + money_sum * deposit.get(time_money)


if __name__ == "__main__":
    print(count_deposit(1000, 6))
    print(count_deposit(1000, 12))
    print(count_deposit(1000, 24))
    print(count_deposit(10000, 6))
    print(count_deposit(10000, 12))
    print(count_deposit(10000, 24))
    print(count_deposit(100000, 6))
    print(count_deposit(100000, 12))
    print(count_deposit(100000, 24))

