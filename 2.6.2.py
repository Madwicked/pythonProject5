a = [int(a) for a in input().split()]
b = int(input())
i = 0
k = 0
d = 0
for i in a:
    if b == i:
        print(k, end=' ')
        d = b
    k += 1
if d == 0:
    print('Отсутствует')