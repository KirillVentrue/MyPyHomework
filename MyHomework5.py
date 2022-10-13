задача 1. Создайте программу для игры с конфетами человек против человека.
start = True
while start:
    print("хотите сиграть в игру 'Кто последний возьмет конфету'? ответьте да или нет")
    answer1 = input().lower()
    if answer1 not in ("да", "нет"):
        print("Введите только да или нет")
        continue
    if answer1 == "да":
        print("Вы будете играть с 1.другом или 2. с ботом?")
        answer2 = answer12()
        if answer2 == "1":
            t2.game_candies_bplayers()
        else:
            t2.game_candies_bot()
    else:
        start = False

задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def code_RLE(text):
    if text == "":
        return ""
    cod_text = ""
    count = 0
    char = text[0]
    for i in range(len(text)):
        if text[i] == char:
            count += 1
        else:
            cod_text += str(count) + char
            char = text[i]
            count = 1
    cod_text += str(count) + char
    return cod_text
 
задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
text = input("Введите строку из которой нужно удалить 'абв': ") 
def del_words(text):
    text = list(filter(lambda x: "абв" not in x, text.split()))
    return " ".join(text)
print(del_words(text))
