print('''   1. Пользователь вводит два значения(годы), для каждого значения(года) из диапазона между ними,
выполняется проверка на високосность с выводом соответствующих ответов в консоль("гггг-сообщение")
 ''')
while True:
    try:
        START = int(input("Ведите дату начала проверки: "))
        END = int(input("Введите дату конца проверки: "))
        break
    except ValueError:
        print("Ведите Дату")

n = ""

for i in range(START, END):
    if i % 400 != 0 and i % 100 == 0:
        n = " - Год НЕ высокосный"
    elif i % 4 == 0 or i % 400 == 0:
        n = " - Год высокосный"
    else:
        n = " - Год НЕ высокосный"
    print(str(i) + n)


