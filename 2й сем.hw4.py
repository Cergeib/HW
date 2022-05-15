class Stack:
    def __init__(self):#метод __init__, который будет устанавливать все свойства стека при инициализации,
                        #при появлении каждого нового стека он будет наделяться чем-то.
        self.stack = [] #Чтобы определить свойство класса используем (self)
    def push(self, item): # pp().
        # Он будет принимать self в качестве аргумента,
        # чтобы иметь доступ к только что определенной переменной stack.

        self.stack.append(item) #append() для добавления элемента в конец списка:
    def pop(self): #pop(), удаляtn последний элемент списка.
                    # этот элемент будет сохранён в переменную removed, а затем возвращать переменную.
        if len(self.stack) == 0:#
            # добавkztv условное выражение для проверки этого крайнего случая
            # (Если в стеке нет элементов, метод должен выбросить ошибку или вернуть null.).
            # Для этого перед запуском .pop  используем if, проверяющее, не пуст ли стек.
            #  тип null  — это None, его и возвращаем, если стек пуст.
            return None
        removed = self.stack.pop()
        return removed
    #тестируем
test = Stack()
test.push(5)
test.push(6)
test.push(7)
test.push(8)
#при выводе test.stack, получftм [5, 6, 7,8].
#test.pop()
#test.pop()
#test.pop()
#test.pop()
#Если мы теперь выведем s.stack, мы получим [5,6,7].
#  удалился только последний элемент
print(test.pop())

