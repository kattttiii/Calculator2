import math
import sys

def Start():
    print("1| |Сложить 2 числа")
    print("2| |Вычесть второе из первого")
    print("3| |Перемножить два числа")
    print("4| |Разделить первое на второе")
    print("5| |Возвести в степень N первое число")
    print("6| |Найти квадратный корень из числа")
    print("7| |Найти 1 процент от числа")
    print("8| |Найти факториал из числа")
    print("9| |Найти косинус")
    print("10| |Найти Синус")
    print("11| |Найти тангенс")
    print("12| |Выйти из программы")

    print("Введите действие:")


    id = input()

    while not id.isdigit():
        print("Введите число!")
        id = input()
    
    
    SelectedCase(int(id))

    # SelectedCase(int(id))

def SelectedCase(id):
    id = int(id)
    if id <= 0 or id >= 13:
        print("Неверное действие")
        print("Выберите действие")

        Start()
        return

    if id == 1:
        print("Введи первое число")
        a = int(input())

        print("Введи втрое число")
        b = int(input())
        print("Ответ:")
        print(a + b)

        Start()
    if id == 2:
        print("Введите первое число")
        a = int(input())

        print("Введи второе число")
        b = int(input())
        print("Ответ:")
        print(a - b)

        Start()
    if id == 3:
        print("Введите первое число")
        a = int(input())

        print("Введи второе число")
        b = int(input())

        if a < 1 or b < 1:
            print("Введите число больше 0!")
            print("Выберите действие")

            d = int(input())
            SelectedCase(d)
            return

        print("Ответ:")
        print(a * b)

        Start()
    if id == 4:
        print("Введите первое число")
        a = int(input())

        print("Введи второе число")
        b = int(input())

        if a < 1 or b < 1:
            print("Введите число больше 0!")
            print("Выберите действие")

            d = int(input())
            SelectedCase(d)
            return
        
        print("Ответ:")
        print(a / b)

        Start()
    if id == 5:
        print("Введите первое число")
        a = int(input())

        print("Введи второе число")
        b = int(input())

        if a < 1:
            print("Введите число больше 0!")
            print("Выберите действие")

            d = int(input())
            SelectedCase(d)
            return
        
        print("Ответ:")
        print(a ** b)

        Start()
    if id == 6:
        print("Введите первое число")
        a = int(input())
        
        if a < 1:
            print("Введите число больше 0!")
            print("Выберите действие")

            d = int(input())
            SelectedCase(d)
            return
        
        print("Ответ:")
        print(math.sqrt(a))

        Start()
    if id == 7:
        print("Введите первое число")
        a = int(input())

        if a < 1:
            print("Введите число больше 0!")
            print("Выберите действие")

            d = int(input())
            SelectedCase(d)
            return
        print("Ответ:")
        print(a / 100)

        Start()
    if id == 8:
        print("Введите первое число")
        a = int(input())

        if a < 1:
            print("Введите число больше 0!")
            print("Выберите действие")

            d = int(input())
            SelectedCase(d)
            return
        
        print("Ответ:")
        print(math.factorial(a))

        Start()
    if id == 9:
        print("Введите первое число")
        a = int(input())

        if a < 1:
            print("Введите число больше 0!")
            print("Выберите действие")

            d = int(input())
            SelectedCase(d)
            return
        
        print("Ответ:")
        print(math.cos(a))

        Start()
    if id == 10:
        print("Введите первое число")
        a = int(input())

        if a < 1:
            print("Введите число больше 0!")
            print("Выберите действие")

            d = int(input())
            SelectedCase(d)
            return
        
        print("Ответ:")
        print(math.sin(a))

        Start()
    if id == 11:
        print("Введите первое число")
        a = int(input())
        if a < 1:
            print("Введите число больше 0!")
            print("Выберите действие")

            d = int(input())
            SelectedCase(d)
            return
        
        print("Ответ:")
        print(math.tan(a))

        Start()

    if id == 12:
        print("Пока ^^")
        sys.exit()


Start()