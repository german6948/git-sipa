# number = int(input('Введите число от 0 до 10'))
# while number < 0 or number > 10:
#     print('Неправильно еще раз')
#     number = int(input('введите число от 0 до 10'))
# print(2**2)


# a = 7
# b = 15
# z = a + b
# print(z)
# a, b = 15, 7
# print(z)


print('Медицинская карта')
name = input('Ваше имя: ')
surname = input('Ваша Фамилмя: ')
age = int(input('Ваш возраст: '))
weight = int(input('Ваш вес: '))
if age < 29 and (weight > 50 or weight < 120):
    print('Пациент в хорошем состоянии')
elif age >= 30 and (weight < 50 or weight > 120):
    print('Пациенту требуется начать вести правильный образ жизни')
elif age > 40 and weight < 50 or weight > 120:
    print('Пациенту требуется врачебный осмотр')
