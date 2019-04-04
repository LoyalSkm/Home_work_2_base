print('''	5. При помощи циклов и логики реализовать вывод в консоль фигуры песочных часов из символов "*",
пользователь задаёт высоту и ширину(в количестве элементов).
Примечание: числа, вводимые пользователем должны быть чётными для корректной -"отрисовки".
''')


import numpy

while True:
    try:
        n = int(input("Высота: "))
        d = float(input("Ширина: "))
        if n == 0 or d == 0:
            print("значения не могут быть 0")
        break

    except ValueError:
        print("Ведите Целое число")


s = [n, d]
bl = max(s)/min(s)
bh = min(s)/max(s)

max = max(s)

if max%2 == 0:
    r = int(max)
else:
    r = int(max+1)

if n==d or (n%2 == 0):
    poz1_end = round((1/2)*n)
    poz2_start = poz1_end
elif n>d or n<d:
    poz1_end = round(((1 / 2) * n) - 0.5)
    poz2_start = round(((1 / 2) * n) + 0.5)
# print(poz1_end)
# print(poz2_start)

list_L = [X for X in numpy.arange(1, d+1, bl)]
list_H = [Y for Y in numpy.arange(1, d+1, bh)]
# print(list_L)
# print(list_H)

if n<=d:
    koef = list_L
elif n>d:
    koef = list_H
# print(koef)
poz = -1

poz = poz2_start
for i in range(n-1, 1, -1):
    poz -= 1
    kol = int(round(koef[poz]))
    # print("*" * kol)
    cen = ("*" * kol)
    print(cen.center(r))
    if i == poz1_end:
        break
for i in range(1, n):
    poz += 1
    kol = int(round(koef[poz]))
    # print("*" * kol)
    cen = ("*" * kol)
    print(cen.center(r))
    if i == poz1_end:
        break


