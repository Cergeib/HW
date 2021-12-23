def sequence():#принемает последовательность в ручную
    sequence = input("введите последовательность")
    k= len(sequence)
    k=str(k)
    sequence = sequence.upper()
    d = {}
    for i in a:
        d[i] = sequence.count(i)
    print(d)
    print('количество символов: ' +  k)

def sequence1():#принемает последовательность из файла
    file_name=input('укажите путь к файлу')
    file = open(file_name)
    sequence=file.read()
    k=len(sequence)
    k=str(k)

    sequence = sequence.upper()
    d = {}

    for i in a:
        d[i] = sequence.count(i)
    print(d)
    print('количество символов: ' +  k)

def choice():
    if l ==1:
        sequence1()
    if l ==2:
        sequence()

def alphabet():#
    global a
    a = [input('введите алфавит разделяя кнопкой enter, чтобы закончить, введите stop')]

    for i in a:
        b = 'stop'# стоп слово
        if i == b:# сравнивает элементы списка со стоп словом
            break # останавливает заполение списка если введено стоп слово
        if i != b:
            a.append(input()) # заполняет список
    a = a[:-1]  # уберает стоп слово из списка
    a=[x.upper() for x in a]

def start():
    z=str(input('введите start'))
    global l
    l=int(input('Если вы хотите окрыть файл, то введите 1 если вы хотите указать последовательность в ручную, то 2'))
    if z == 'start':

        alphabet()
        choice()

start()