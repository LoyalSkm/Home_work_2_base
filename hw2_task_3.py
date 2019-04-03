print('''   3. "Нарисовать" в консоли прямоугольный треугольник из символов "*",
пользователь задаёт высоту и ширину(в количестве элементов).
''')
print('''Задавай какую хочешь высоту НО ПОМНИ сколько * влезет в эту высоту такой ширина и будит
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

list_L = [X for X in numpy.arange(1, d+1, bl)] #список для случая высоты больше ширины
list_H = [Y for Y in numpy.arange(1, d+1, bh)] #навпакы)


if n<=d:                                      #список для обоих случаев
    koef = list_L
elif n>d:
    koef = list_H

poz = -1                                      #переменная старта звёздочек
for i in range(1, n+1):
    poz += 1
    kol = int(round(koef[poz]))               #типо позиция в списках list_H или list_L
    print("*" * kol)                          #строим трыкутнык)


# import numpy
#
# print("Printing float range with numpy.arange()")
# print("Example one")
# for i in numpy.arange(0, 5.5, 0.5):
#     print(i, end=', ')
# print("\nExample two")
# for i in numpy.arange(5.5, 15.5, 2.5):
#     print(i, end=', ')
# print("\nExample Three")
# for i in numpy.arange(-2.5, 2.5, 0.5):
#     print(i, end=', ')