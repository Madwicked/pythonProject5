a = int(input())
i = a ** 2
s = a
while s != 0:
    a = int(input())
    i += a ** 2
    s += a
print(i)
