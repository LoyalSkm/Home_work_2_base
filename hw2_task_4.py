print('''   4. При помощи циклов и логики реализовать вывод в консоль ромба из символов "*",
пользователь задаёт высоту и ширину(в количестве элементов).
''')


import numpy

while True:
    try:
        n = int(input("Высота: "))
        d = float(input("Ширина: "))
        break
    except ValueError:
        print("Ведите Целое число")
s = [n, d]
bl = max(s)/min(s)   #коефициент для случая когда высота больше ширины
bh = min(s)/max(s)   #когда ширина больше высоты

max = max(s)        # Не знаю, почемуто не идет проверка на чётность есть не сделать переменной(

if max%2 == 0:      #условие для того чтобы сцентрировать ромб относительно максимального значения
    r = int(max)
else:
    r = int(max+1)

if n==d or (n%2 == 0):                #Тут мы находим отношение сторон ромба типо если 11 по высоте то центр должен быть
    poz1_end = round((1/2)*n)         #в позиции 6 и ромб делится на 2 участка 5 и 6, а если высота это чётное число
    poz2_start = poz1_end             #то стороны одинаковы
elif n>d or n<d:
    poz1_end = round(((1 / 2) * n) - 0.5)
    poz2_start = round(((1 / 2) * n) + 0.5)
# print(poz1_end)
# print(poz2_start)

list_L = [X for X in numpy.arange(1, d+1, bl)] #список для случая высоты больше ширины
list_H = [Y for Y in numpy.arange(1, d+1, bh)] #навпакы)
# print(list_L)
# print(list_H)

if n<=d:                                      #Тут я делаю 1 переменную которая меняется от случая n<d и n>=d
    koef = list_L
elif n>d:
    koef = list_H
# print(koef)
poz = -1                                      #переменная старта звёздочек
for i in range(1, n):
    poz += 1
    kol = int(round(koef[poz]))               #типо позиция в списках list_L или list_LL
    # print("*" * kol)
    cen = ("*" * kol)                          #строим ромб)
    print(cen.center(r))              #центрируем звёзды относительно максимального значения ширины
    if i == poz1_end:                          #заканчиваем цыкл в позиции которую раньше узнали для пропорции, ну и закрутил.
        break
poz = poz2_start                               #начало "спада" ромба, не знаю как жто назвать, ну типо с центра к 1..
for i in range(n-1, 1, -1):                    #обратный цыкл
    poz -= 1
    kol = int(round(koef[poz]))
    # print("*" * kol)
    cen = ("*" * kol)
    print(cen.center(r))
    if i == poz1_end:
        break




