# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# def stepen(A, B):
#     if(A>0 and B>0):
#         return A**B
#     return 0
# print("Введите A: ")
# A = int(input())
# print("Введите B: ")
# B = int(input())
# print(stepen(A, B))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# def summa(a, b):
#     a = a+1
#     b = b-1
#     if b>0:
#         return summa(a,b)
#     else: return a
# print("Введите а: ")
# a = int(input())
# print("Введите b: ")
# b = int(input())
# print(summa(a, b))