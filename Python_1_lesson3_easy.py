__author__ = 'Герман Дмитрий Юрьевич'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    return round(number, ndigits)
     
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):

    ticket_list = []
    left_sum = 0
    right_sum = 0
    while ticket_number > 0:
        ticket_list.append(ticket_number % 10)
        ticket_number //= 10
    for i in range(3):
        left_sum += ticket_list[i]
        right_sum += ticket_list[i+3]
    if left_sum == right_sum:
        return 'Lucky ticket!'
    else:
        return 'Try again!'

print(lucky_ticket(123006))
print(lucky_ticket(123214))
print(lucky_ticket(436751))
