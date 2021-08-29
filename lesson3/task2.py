"""2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они
совпадают, программа должна возвращать значение True, иначе False. """


try:
    my_num = input("Введите число Float или Int: ")
    print(f"Число - {int(my_num)} - Целое")

except ValueError:
    try:
        main_part = my_num.split('.')[0]
        the_rest_part = my_num.split('.')[1]

        print(f"Число - {float(my_num)} - Дробное\n"
              f"Целая часть: {main_part} \n"
              f"Дробная часть: {the_rest_part}\n"
              f"Равенство дробной и целой частей: {int(main_part) == int(the_rest_part)}")

    except ValueError:
        print("Вы ввели число не Float или Int!")
    except IndexError:
        print("Вы ввели число не Float или Int!")

