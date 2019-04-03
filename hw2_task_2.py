print('''   2. Пользователь вводит два значения(диапазон), вычисляется среднее арифметическое, если число парное,
выводим пользователю ответом "2" и половину среднего арифметического, в случае нечётного среднего арифметического 
выводится пара из числа 1 и среднего арифметического.
''')
while True:
    try:
        FIRST = float(input(">>"))
        SECOND = float(input(">>"))
        break
    except ValueError:
        print("Ведите Число")

list = []                  #пустой список
calc = FIRST               #начало диапазона

while calc <= SECOND:
    list.append(calc)      #добавление значения calc в список
    calc = int(calc) + 1

res = sum(list)/len(list) #sum(list) - сумма всех значений в диапазоне
                          #len(list) - количество итемов в списке'''

if res % 2 == 0:
    print("2 - " + str(res))
else:
    print("1 - " + str(res))


