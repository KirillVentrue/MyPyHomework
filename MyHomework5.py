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
