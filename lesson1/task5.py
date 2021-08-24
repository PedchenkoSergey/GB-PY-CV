"""5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться
фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию
подсчета процентов для пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца,
кроме первого и последнего. Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами), а главная функция — общую сумму по
вкладу на конец периода. """


def count_deposit(money_sum: int, time_money: int, add_money: int) -> str:
    """
    :param money_sum:
    :param time_money:
    :param add_money:
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

    def monthly_add(time, add, proc):
        return (add * (time - 2)) + time * (time - 2) * add * proc / 12

    for deposit in deposits:
        if deposit.get("begin_sum") <= money_sum < deposit.get("end_sum"):
            if time_money <= 12:
                tot_money = money_sum + \
                money_sum * deposit.get(time_money) * time_money / 12
                tot_proc = monthly_add(time_money, add_money, deposit.get(time_money))
                return f"Вклад с изначальной суммой: {money_sum}, на срок: {time_money} месяцев\n" \
                       f"Ежемесячное пополнение: {add_money}\n" \
                       f"Доход по пополнениям: {tot_proc}, процентная ставка: {deposit.get(time_money)}\n" \
                       f"Доход по основному депозитарному счету включая проценты на пополнение: {tot_money + tot_proc}\n"

            # Считаем с капитализацией основного счета и без для процентов:
            if time_money == 24:
                init_money_sum = money_sum
                money_sum = money_sum + money_sum * deposit.get(time_money)
                tot_money = money_sum + \
                money_sum * deposit.get(time_money)
                tot_proc = monthly_add(time_money, add_money, deposit.get(time_money))

                return f"Вклад с изначальной суммой: {init_money_sum}, на срок: {time_money} месяцев\n" \
                       f"Ежемесячное пополнение: {add_money}\n" \
                       f"Доход по пополнениям: {tot_proc}, процентная ставка: {deposit.get(time_money)}\n" \
                       f"Доход по основному депозитарному счету включая проценты на пополнение: {tot_money + tot_proc}\n"


if __name__ == "__main__":
    print(count_deposit(1000, 6, 100))
    print(count_deposit(1000, 12, 100))
    print(count_deposit(1000, 24, 100))
    print(count_deposit(10000, 6, 1000))
    print(count_deposit(10000, 12, 1000))
    print(count_deposit(10000, 24, 1000))
    print(count_deposit(100000, 6, 10000))
    print(count_deposit(100000, 12, 10000))
    print(count_deposit(100000, 24, 10000))
