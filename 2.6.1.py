n = int(input())
a = 0
i = []
c = 0
while a != n:
    a += 1
    c = [a] * a
    i += c
    #print(i[:n], end = ' ')
print(*i[:n])