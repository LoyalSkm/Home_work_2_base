print('''   3. "Нарисовать" в консоли прямоугольный треугольник из символов "*",
пользователь задаёт высоту и ширину(в количестве элементов).
''')
print('''Задавай какую хочешь высоту, но триугольник будит пропорциональным только если высота<ширины в 2 раза
''')
import numpy  #позволит мне сделать список из е целых чисел

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
max = max(s)
if max%2 == 0:       #условие для того чтобы сцентрировать триугольник относительно максимального значения
    r = int(max)
else:
    r = int(max+1)

list_L = [X for X in numpy.arange(1, d+1, bl)] #список для случая высоты больше ширины
list_H = [Y for Y in numpy.arange(1, d+1, bh)] #навпакы)
# print(list_L)
# print(list_H)
if n<=d:                                      #Тут я делаю 1 переменную которая меняется от случая n<d и n>=d
    koef = list_L
elif n>d:
    koef = list_H

poz = -1                                      #переменная старта звёздочек
for i in range(1, n+1):
    poz += 1
    kol = int(round(koef[poz]))               #типо позиция в списках list_L или list_LL
    # print("*" * kol)
    cen = ("*" * kol)                          #строим трыкутнык)
    print(cen.center(r))

