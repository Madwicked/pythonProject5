{(a=input()
b = []
c = []
l = 1  # len(a.split())
print(l)
while a != 'end':
    b.append([int(i) for i in a.split()])
    a = input()
c = b
for i in range(l):
    for j in range(l):
        c[i][j] = b[(i - 1) % l][j] + b[(i + 1) % l][j] + b[i][(j - 1) % l] + b[i][(j + 1) % l]
        # c[i][j] = b[i][j]+1
        # j += 1
        print(c[i][j], end=' ')
    print() )}


string = m = []
while string != 'end':
    string = input()
    m.append(list(map(int, string.split(' ')))) if string != 'end' else None
li, lj = len(m), len(m[0])
new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]
[print(' '.join(map(str, row))) for row in new]