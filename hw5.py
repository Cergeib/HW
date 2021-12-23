def n_sort(y):
    for i in range(1, len(y)): #i  будет исчисляться от 1 до (длины списка - 1)

        temp = y[i]
        j = i - 1
        while (j >= 0 and temp < y[j]): #будет работать до тех пор, пока j не отрицательное и temp меньше, чем элемент под индексом j
            y[j + 1] = y[j]
            j = j - 1
        y[j + 1] = temp


y = input('Введите список 'ktvtynjd': ').split()
y = [int(x) for x in y]
n_sort(y)
print('Отсортированный список: ', end='')
print(y)
