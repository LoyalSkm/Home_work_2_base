print('''   4. При помощи циклов и логики реализовать вывод в консоль ромба из символов "*",
пользователь задаёт высоту и ширину(в количестве элементов).
''')

while True:
    try:
        n = int(input("Высота: "))
        d = int(input("Ширина: "))
        break
    except ValueError:
        print("Ведите Целое число")
s = [n, d]
p = 0
r = max(s)
bl = max(s)/min(s)
bh = min(s)/max(s)
if n < d:
    p = bh
elif n > d:
    p = round(bl)
elif n == d:
    p = 1
print(p) #коефициент по которому потом выщитуются *

for i in range(1, n, 2): #* на увеличение
    if i>=d:
        i = d
        s = "*" * round(i*p)
        print(s.center(r))
    else:
        s = "*" * round(p*i)
        print(s.center(r))
for i in range(n, 0, -2): #* на уменьшение
    if i>=d:
        i = d
        s = "*" * round(i*p)
        print(s.center(r))
    else:
        s = "*" * round(p*i)
        print(s.center(r))
