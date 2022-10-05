Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
*Пример:*
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
  
list = [2, 3, 5, 9, 3]
sum = 0
for i in range(len(list)):
    if (i % 2 != 0):
        sum += list[i]
print(f"Сумма нечетных элементов списка = {sum}")

Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

def sum_element(list):
    result = []
    for i in range(len(list)):
        if (i > len(list) - i - 1):
            break
        result.append(list[i] * list[len(list) - i - 1])
    return result

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
print(f"Сумма первой пары = {sum_element(list1)}")
print(f"Сумма второй пары = {sum_element(list2)}")

Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
*Пример:*
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def difference(list):
    min = 1
    max = 0
    for i in range(len(list)):
        temp = float("0." + str(round((list[i]), 2)).split('.')[1])
        if min > temp:
            min = temp
        elif max < temp:
            max = temp
    print(f"Минимальный элемент списка {min}")
    print(f"Максимальным элемент списка {max}")
    return (max - min)
list = [1.1, 1.2, 3.1, 5.17, 10.02]
print(f"Разница между мин и макс значением списка = {round(difference(list), 2)}")

Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*
- 45 -> 101101
- 3 -> 11
- 2 -> 10

def binary(number):
    result = ""
    temp = number % 2
    if (temp == 0):
        result = "0" + result
        number = number / 2
    elif (temp == 1):
        result = "1" + result
        number = (number - 1) / 2
    if(number != 1):
        return result + binary(number)
    else: 
        result = "1" + result
        return result

number = int(input(print("Введите целое число: ")))
print(f"Результат преобразования {number} = {binary(number)}")
