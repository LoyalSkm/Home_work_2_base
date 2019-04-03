print('''   3. "Нарисовать" в консоли прямоугольный треугольник из символов "*",
пользователь задаёт высоту и ширину(в количестве элементов).
''')
print('''Задавай какую хочешь высоту НО ПОМНИ сколько * влезет в эту высоту такой ширина и будит
''')
while True:
    try:
        n = int(input("Высота: "))
        d = int(input("Ширина: "))
        break
    except ValueError:
        print("Ведите Целое число")
s = [n, d]
bl = round(max(s)/min(s))
t = max(s)

for i in range(1, n+1, bl):
        p = i / t
        # print(p)
        s = "*"*round(p*i)
        # print(s)
        print(str(i) + s)