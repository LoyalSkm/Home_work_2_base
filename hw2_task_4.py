print('''   4. При помощи циклов и логики реализовать вывод в консоль ромба из символов "*",
пользователь задаёт высоту и ширину(в количестве элементов).
''')

n = int(input("Высота: "))
d = int(input("Ширина: "))
if n % 2 == 0:
    n -= 1
for i in range(1, n + 1, 2):
    if i>=d:
        i=d
        s = "*"*i
        print(s.center(d))
    else:
        s = "*" * i
        print(s.center(d))
for i in range(n-2, 0, -2):
    if i>=d:
        i=d
        s = "*"*i
        print(s.center(d))
    else:
        s = "*" * i
        print(s.center(d))
