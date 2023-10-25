# 1.Написать программу сложения двух чисел. Числа вводятся пользователем.
# n1 = float(input("Enter number1: "))
# n2 = float(input("Enter number2: "))
# summa = n1 + n2
# print(f"summa: {n1} + {n2} = {summa}")


#2.Написать программу сравнения двух строк. Строки вводятся пользователем. Строку,которая будет больше лексикографически другой, вывести как результат
# str1 = input("Enter the first line: ")
# str2 = input("Enter the second line: ")
# if str1 < str2:
#     print(f"Result: '{str2}' > '{str1}'") 
# elif str1 > str2:
#     print(f"Result: '{str1}' > '{str2}'")
# else:
#     print("The lines are identical.")

#3.Написать программу которая выполняет следующую операцию a%b. Числа вводятся пользователем. Если результат операции равен 1, вывести уведомление, в другомслучае вывести остаток.

# a = int(input("a: "))
# b = int(input("b: "))
# x = a % b
# if x == 1:
#     print("a % b = 1.")
# else:
#     print(f"a % b = {x}.")

#4Написать программу, которая определяет наличие введенного значения в данномсписке. Значение вводится отдельно. Результат программы вывести уведомлением.list = [1,2,3,4,5,6]
list = [1, 2, 3, 4, 5, 6]
v = int(input("Enter a search value: "))
if v in list:
    print(f"{v} on the list.")
else:
    print(f"{v} not listed.")





