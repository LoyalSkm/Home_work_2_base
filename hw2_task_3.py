print('''   3. "Нарисовать" в консоли прямоугольный треугольник из символов "*",
пользователь задаёт высоту и ширину(в количестве элементов).
''')
print('''Задавай какую хочешь высоту НО ПОМНИ сколько * влезет в эту высоту такой ширина и будит
''')
n = int(input("Высота: "))
d = int(input("Ширина: "))
s = [n, d]
bl = max(s)/min(s)
bh = min(s)/max(s)
print("*")
if n == d:
    for i in range(2, n+1):
        s = "*"*round(i)
        print(s)
if n < d:
    for i in range(2, n+1):
        s = "*"*round(i*bl)
        print(s)
if n > d:
    for i in range(2, n+1):
        s = "*"*round(i*bh)
        print(s)