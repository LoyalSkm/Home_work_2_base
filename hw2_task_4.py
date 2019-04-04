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
if n>d or n<d:
    poz1_end = round(((1 / 2) * n) - 0.5)
    poz2_start = round(((1 / 2) * n) + 0.5)
elif n==d:
    poz1_end = round((1/2)*n)
    poz2_start = poz1_end


s = [n, d]
bl = (max(s)/min(s))
bh = (max(s)/min(s))
max = max(s)
if max%2 == 0:
    r = int(max)
else:
    r = int(max+1)

list_L = [X for X in numpy.arange(1, poz1_end+1, 1)] #список для случая высоты больше ширины
list_LL = [X for X in numpy.arange(poz2_start, 0, -1)] #список для случая высоты больше ширины

new_L = [X for X in numpy.arange(1, d+1, n/(n/2))]
new_LL = [X for X in numpy.arange(d-1, 0, -(n/(n/2)))]

new_list_L = [X *bh for X in list_L]
new_list_LL = [X *bh for X in list_LL]

print(bl)
print(bh)
print(list_L)
print(list_LL)

print(new_L)
print(new_LL)

print(new_list_L)
print(new_list_LL)
print(poz1_end)
print(poz2_start)

poz1 = -1

for i in range(1, poz1_end+1):
    poz1 += 1
    kol = int(round(new_L[poz1]))               #типо позиция в списках list_H или list_L
    s = "*" * round(kol)
    print(s.center(r))
pp = "*" * r
poz1 = -1
for i in range(poz2_start, 0, -1):
    poz1 += 1
    kol = int(round(new_LL[poz1]))               #типо позиция в списках list_H или
    s = "*" * round(kol)
    print(s.center(r))



# s = [n, d]
# p = 0
# r = max(s)
# bl = max(s)/min(s)
# bh = min(s)/max(s)
# if n < d:
#     p = bh
# elif n > d:
#     p = round(bl)
# elif n == d:
#     p = 1
# print(p) #коефициент по которому потом выщитуются *
#
# for i in range(1, n, 2): #* на увеличение
#     if i>=d:
#         i = d
#         s = "*" * round(i*p)
#         print(s.center(r))
#     else:
#         s = "*" * round(p*i)
#         print(s.center(r))
# for i in range(n, 0, -2): #* на уменьшение
#     if i>=d:
#         i = d
#         s = "*" * round(i*p)
#         print(s.center(r))
#     else:
#         s = "*" * round(p*i)
#         print(s.center(r))

