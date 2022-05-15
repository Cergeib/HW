q=input('укажите полный путь к файлу')
file1 = open(q, "r")
def read_file(file1):
    while True:
    # считываем строку
        line = file1.readline()
    # прерываем цикл, если строка пустая
        if not line:
            break
    # выводим строку
        print(line.strip())

# закрываем файл
    file1.close

read_file(file1)

