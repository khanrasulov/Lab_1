a = int(input("Введите радиус первого круга: "))
b = int(input("Введите радиус второго круга: "))


rez = ''
if a > b:
    rez = 'Радиус первого круга больше, чем второго'
elif a == b:
    rez = 'Радиусы кругов одинаковы'
else:
    rez = 'Радиус второго круга больше, чем первого'


sq_a = 3.14 * a**2
sq_b = 3.14 * b**2

if a > b:
    df_sqa = sq_a - sq_b
    dfsq = df_sqa
else:
    df_sqb = sq_b - sq_a
    dfsq = df_sqb

if a > b:
    df_sqaq = sq_a**2 - sq_b**2
    dfsqq = df_sqaq
else:
    df_sqbq = sq_b**2 - sq_a**2
    dfsqq = df_sqbq

print(rez)
print('Разность площадей: ', dfsq)
print(f"Разность площадей квадратов: {dfsqq:.2f}")





