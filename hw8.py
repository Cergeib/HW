import random
def random1():
  x = input('Выберете последовательность: РНК, ДНК или Последовательность аминокислот ')
  y=int(input('введите длинну последовательности'))
  x= x.upper()
  def gen (w):
    t = ''.join(random.choice(w) for i in range(y))
    return t
    print(t)
  RNA = ['A', 'U', 'G', 'C']
  DNA = ['A', 'T', 'G', 'C']
  AaS = ['G', 'L', 'Y', 'S','E', 'Q', 'D', 'N','F', 'A', 'K', 'R', 'H', 'C', 'V', 'P','W', 'I', 'M','T']

  if x == 'DNA'or x=='ДНК'or x=='1':
    print('Сгенерирована последовательность ДНК -', gen(DNA))
  elif x == '2'or x== 'RNA'or x=='РНК':
    print('Сгенерирована последовательность РНК -', gen(RNA))
  elif x == '3'or x== 'ПОСЛЕДОВАТЕЛЬНОСТЬ АМИНОКИСЛОТ':
    print('Сгенерирована последовательность из аминокислот -', gen(AaS))
  else:
    print('Error: Неверный запрос!! повторите ввод')

random1()