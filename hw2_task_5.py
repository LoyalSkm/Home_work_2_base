print('''	5. При помощи циклов и логики реализовать вывод в консоль фигуры песочных часов из символов "*",
пользователь задаёт высоту и ширину(в количестве элементов).
Примечание: числа, вводимые пользователем должны быть чётными для корректной -"отрисовки".
''')
while True:
    try:
        H = int(input("Высота: "))
        L = int(input("Ширина: "))
        break
    except ValueError:
        print("Ведите Целое число")

s = [H, L]
bl = max(s)/min(s)
bh = min(s)/max(s)

if H < L:
    p = bh
elif H > L:
    p = bl
elif H == L:
    p = 1

for i in range(H, 1, -2):
    if i>=L:
        i = L
        s = "*" * round(i*p)
        print(s.center(L))
    else:
        s = "*" * round(p*i)
        print(s.center(L))

for i in range(1, H+1, 2):
    if i>=L:
        i = L
        s = "*" * round(i*p)
        print(s.center(L))
    else:
        s = "*" * round(p*i)
        print(s.center(L))

