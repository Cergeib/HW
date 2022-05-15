from prettytable import PrettyTable  # Импортируем установленный модуль.

from collections import Counter
a = open(input('введите путь к файлу')).read().split('\n')[0:]# открытие файла
name=a[0]                                        #первая строка имя

print('name ' + name)
sequences=a[1:]                                  #вырезаем последовательность
concatenated_sequence = ''.join(sequences)       #объеденяем список для подсчёта нуклеотидов

sequence_length = len(concatenated_sequence)     #считаем количество нуклеотидов

print('количество нуклеотидов ' + str(sequence_length))
c = Counter(concatenated_sequence)                #считаем вхождение АТGС нуклеотиды


A=c["A"]                                          #считаем А
T=c["T"]                                          #считаем В
G=c["G"]                                          #считаем G
C=c["C"]                                          #считаем С
U=c["U"]                                          #считаем U
GC=concatenated_sequence.count('GC')
GC= GC*100/sequence_length
GC=round(GC,1)
print("A=" + str(A))
print("T=" + str(T))
print("G=" + str(G))
print("C=" + str(C))
print("U=" + str(U))
print("%GC=" + str(GC))




th = ['name', 'sequence length', 'A', 'T', 'G','C','U', '%GC' ] # Определяем шапку и данные.
td = [name, sequence_length, A, T, G, C, U, GC] # Определяем шапку и данные.

columns = len(th)  # Подсчитаем кол-во столбцов на будущее.

table = PrettyTable(th)  # Определяем таблицу.


td_data = td[:] # Cкопируем список td
# Входим в цикл который заполняет нашу таблицу.
# Цикл будет выполняться до тех пор пока у нас не кончатся данные
# для заполнения строк таблицы (список td_data).
while td_data:
    # Используя срез добавляем первые пять элементов в строку.
    # (columns = 5).
    table.add_row(td_data[:columns])
    # Используя срез переопределяем td_data так, чтобы он
    # больше не содержал первых 5 элементов.
    td_data = td_data[columns:]

print(table)  # Печатаем таблицу