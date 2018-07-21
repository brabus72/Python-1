
__author__ = 'Герман Дмитрий Юрьевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

x = int(input('Введите произвольное целое число: '))
x = abs(x)
print('Цифры числа в обратном порядке:')
while True:
    print(x % 10) 
    x = x // 10
    if x == 0: 
        break 
	    
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input('Введите значение переменной 1: '))
b = int(input('Введите значение переменной 2: '))

temp = a + b
a = temp - a
b = temp - b

print('Новое значение переменной 1: ', a)
print('Новое значение переменной 2: ', b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Введите Ваш возраст: '))

if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')

