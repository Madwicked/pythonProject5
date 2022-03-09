a =[]
b=[]
n = int(input())
for i in range ((n ** 2) +1):
     b.append(i)
print(b)
for i in range(n):
    a.append([0]* n)
for i in range(n):

    for j in range(n):
       a[i][j] = b[i +1]

    print(a[i][j], end = '')
