# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

# i = 1
# while i <= 5:
#     print(i, "0000000")
#     i = i + 1

# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.

# j = 0
# i = 1
# while i <= 10:
#     number = input("Введите число")
#     number = int(number)
#     i = i + 1
#     if number == 5:
#         j = j + 1
#     else:
#         continue
#
# print('Количество цифр 5 =', j)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# num = 1
# for i in range(1,11):
#     num*=i
# print(num)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# integer_number = 6542
# sum = 0
# while integer_number>0:
#     sum = sum + integer_number%10
#     integer_number = integer_number//10
# print('Сумма цифр числа =',sum)
'''
Задача 7
Найти произведение цифр числа.
'''
# integer_number = 584
# num = 1
# while integer_number>0:
#     num *= integer_number%10
#     integer_number = integer_number//10
# print('Произведение цифр числа =',num)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number > 0:
#     if integer_number % 10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number // 10
# else:
#     print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# max_number = 0
# integer_number = 6489
# while integer_number > 0:
#     if max_number < integer_number % 10:
#         max_number = integer_number % 10
#     integer_number = integer_number // 10
# print('Максимальная цифра в числе -', max_number)
'''
Задача 10
Найти количество цифр 5 в числе
'''
# sum = 0
# integer_number = input('Введите целое число')
# integer_number = int(integer_number)
# while integer_number > 0:
#     if integer_number % 10 == 5:
#         sum = sum + 1
#
#     integer_number = integer_number // 10
# print('Количество цифр 5 в числе -',sum)