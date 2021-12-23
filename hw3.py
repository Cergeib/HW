import math

def triangle1():
    a=int(input('Введите сторону a '))
    h=int(input('Введите высоту '))
    s=1/2*a*h
    print('площадь = ' + str(s))
def polygon():
    a=int(input('введите длинну стороны'))
    b=int(input('введите количество сторон'))
    print( (a ** 2 * b) / (4 * math.tan(math.pi / b)))

def rectangle():
    a=int(input('Введите сторону a '))
    b=int(input('Введите сторону b '))
    s= a*b
    print('площадь = ' + str(s))

def trapezoids1():
    a=int(input('Введите основание a '))
    b=int(input('Введите основание b '))
    h=int(input('Введите высоту '))
    s=0.5*(a+b)*h
    print('площадь = ' + str(s))

def circle1():
    r=int(input('Введите целочисленный радиус '))
    q=r**2
    s=q*3.14
    print('площадь = ' + str(s))
def figures():
    figure=int(input("""Для рассчета площади, выберите номер который соответствует фигуре для необходимого вам рассчета 
1-Произвольный треугольник
2-Прямоугольник
3-Трапеция
4-Круг
5-Правильный многоугольник
"""))
    if figure == 1:
        print('Вы выбрали треугольник')
        triangle1()
    if figure == 2:
        print('Вы выбрали прямоугольник')
        rectangle()
    if figure == 3:
        print('Вы выбрали трапеция')
        rectangle()
    if figure == 4:
        print('Вы выбрали круг')
        circle1()
    if figure == 5:
        polygon()
        print('Вы выбрали многоугольник')
figures()

