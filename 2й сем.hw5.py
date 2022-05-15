import re
a = open(input('укажите путь к файлу')).read().split('\n')[0:]# открытие файла
sequences=a[1:]                                  #вырезаем последовательность
concatenated_sequence = ''.join(sequences)#объеденяем список в строку для поиска кодонов
str1 = concatenated_sequence  # наша последовательность для анализа
list1 = []  # лист, в который добавляем рамки
items1 = re.findall(r'.{3}', str1)
items2 = re.findall(r'.{3}', str1[1:])  # делим строку на 3 списка
items3 = re.findall(r'.{3}', str1[2:])

for i in range(len(items1) - 1):  # ищем рамки длинее 102 кодонов в первом списке
    if items1[i] == 'ATG':  # проверка, соответствует ли i-й элемент старт-кодону
        tr = items1[i:]  # новый список, начинается со старт кодона, который мы нашли
        for j in range(len(tr) - 1):  # ищем стоп-кодон по новому списку
            b = tr[j]
            if b == 'TAA' or b == 'TGA' or b == 'TAG':  # если текущий элемент - стоп кодон - идем вниз по телу цикла
                if len(items1[i:i + j + 1]) >= 102:  # проверяем, длинее ли получившийся список 102 кодонов
                    list1.append(items1[i:i + j + 1])
                break

for i in range(len(items2) - 1):  # во втором
    if items2[i] == 'ATG':
        tr = items2[i:]
        for j in range(len(tr) - 1):
            b = tr[j]
            if b == 'TAA' or b == 'TGA' or b == 'TAG':
                if len(items2[i:i + j + 1]) >= 102:
                    list1.append(items2[i:i + j + 1])
                break

for i in range(len(items3) - 1):  # в третьем
    if items3[i] == 'ATG':
        tr = items3[i:]
        for j in range(len(tr) - 1):
            b = tr[j]
            if b == 'TAA' or b == 'TGA' or b == 'TAG':
                if len(items3[i:i + j + 1]) >= 102:
                    list1.append(items3[i:i + j + 1])
                break

print(len(list1))  # количество рамок
print(list1)  # выводит список, в котором содержатся все рамки
