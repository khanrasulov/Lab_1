name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
sch = input("Введите номер вашей школы: ")
cl = int(input("Какой класс вы окончили?: "))
cl_letter = input("Введите букву класса: ")



if cl == 11:
    end = 2023 - (18 - age)
elif cl == 9:
    end = 2023 - (18 - age)


if cl == 9 or cl == 11:
    print(f'''
Привет {name}!
Поздравляю с окончанием {cl}{cl_letter} класса школы №{sch}
в {end} году.''')
else:
    print('Введен не тот класс ')
