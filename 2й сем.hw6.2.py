
import re
from collections import Counter
try:

    a = open(input('укажите путь к файлу')).read().split('\n')[0:]# открытие файла
    sequences=a[1:]                                  #вырезаем последовательность
    concatenated_sequence = ''.join(sequences)#объеденяем список в строку для поиска кодонов
    str1 = concatenated_sequence  # наша последовательность для анализа
    sequence_length = len(str1)#длинна последовательности



    list1 = []  # лист, в который добавляем рамки
    items1 = re.findall(r'.{3}', str1)
    items2 = re.findall(r'.{3}', str1[1:])  # делим строку на 3 списка
    items3 = re.findall(r'.{3}', str1[2:])
    def ww(aj):
        for i in range(len(aj) - 1):  # ищем рамки длинее 102 кодонов в первом списке
            if aj[i] == 'ATG':  # проверка, соответствует ли i-й элемент старт-кодону
                tr = aj[i:]  # новый список, начинается со старт кодона, который мы нашли
                for j in range(len(tr) - 1):  # ищем стоп-кодон по новому списку
                    b = tr[j]
                    if b == 'TAA' or b == 'TGA' or b == 'TAG':  # если текущий элемент - стоп кодон - идем вниз по телу цикла
                        if len(aj[i:i + j + 1]) >= 102:  # проверяем, длинее ли получившийся список 102 кодонов
                            list1.append(aj[i:i + j + 1])
                        break


    def www ():

        ww(items1)
        ww(items2)
        ww(items3)


    www()


    print(len(list1))  # количество рамок
    print(list1)  # выводит список, в котором содержатся все рамки
    print(len(list1))  # количество рамок



except:
    print("не верный путь! ")
