задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def mult(num):
    i = 2
    list = []
    while i <= num:
        if not num % i:
            list.append(i)
            num //= i
            i = 2
        else:
            i += 1
    return list
print(mult(int(input("Введите число: "))))

задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def without_repeat_elements(list):
    res = []
    for i in range(len(list)):
        if not((list[i] in list[0:i]) or (list[i] in list[i+1:])):
            res.append(list[i])
    return res
lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(without_repeat_elements(lst))

задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
*Пример:* 
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
def polynom(k):
    r = random.randint(0, 100)
    count = ""
    if k > 0:
        if r > 0: f.write(f'{r} * x^{k} + ")
        return polynom(k-1)
    if r > 0: count = str(r)
    return count+" = 0"
k = int(input("Задайте натуральную степень: "))
f = open("exam4.txt", "w")
f.write(polynom(k))
f.close
