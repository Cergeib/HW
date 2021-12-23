
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


def random2():
  import random
  x = input('Выберете последовательность: РНК, ДНК или Последовательность аминокислот ')
  x= x.upper()
  def gen (w):
    t = ''.join(random.choices(w, k=random.randint(10, 1000)))
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

def sequence_generator():
  l=int(input('1-пользовательская длинна последовательности,2 случайная длинна последовательности'))
  if l==1:
    random1()
  elif l==2:
    random2()
sequence_generator()