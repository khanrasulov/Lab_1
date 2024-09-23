a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

summa = a + b
calcul = a * b
sr_arf = (a + b)/2

if a >= b:
    dif_1 = a - b
    razn = dif_1
else:
    dif_2 = b - a
    razn = dif_2

al = a
bl = b
if a < 0:
    al = -a
elif b<0:
    bl = -b

if al >= bl:
    modul = al - bl
else:
    modul = bl - al

if a >= b:
    dif_33 = a**2 - b**2
    sq_razn = dif_33
else:
    dif_3 = b**2 - a**2
    sq_razn = dif_3

print('Сумма: ', summa)
print('Разность: ', razn)
print('Произведение: ', calcul)
print('Среднее арифметическое: ', sr_arf)
print('Разность max и min по модулю: ', modul)
print('Разность квадратов: ', sq_razn)

