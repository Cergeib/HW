1
задание
a = int(input())
if a % 2 == 0:
    print("Чётное")
else:
    print("нечётное")
2
задание

a = int(input())
b = int(input())
print(a + b)

3
задача
n = int(input())
q = []
for i in range(2, n + 1):
    k = 0
    for j in q:
        if i % j == 0:
            k = 1
    if k == 0:
        q.append(i)
q = q[-1]
q = str(q)
print(q)

4
задача
n = int(input())
print(end=" ")
for i in range(n - 1, 1, -1):
    k = 0
    if (n % i == 0):
        for j in range(i - 1, 1, -1):
            if (i % j == 0):
                k = k + 1
        if (k == 0):
            print(i, end=" ")

5
задача
n = int(input())
q = []
for i in range(2, n + 1):
    k = 0
    for j in q:
        if i % j == 0:
            k = 1
    if k == 0:
        q.append(i)
f1 = q[0]
f2 = q[-1]

p = 15  # количество подсчётов

print(f1, f2, end=' ')

for i in range(2, p + 1):
    f1, f2 = f2, f1 + f2
    print(int(f2), end=' ')

Вариант
2
n = int(input())
q = []
for i in range(2, n + 1):
    k = 0
    for j in q:
        if i % j == 0:
            k = 1
    if k == 0:
        q.append(i)
f1 = q[-1]
f2 = f1

p = 15  # количество подсчётов

print(f1, f2, end=' ')

for i in range(2, p + 1):
    f1, f2 = f2, f1 + f2
    print(int(f2), end=' ')


