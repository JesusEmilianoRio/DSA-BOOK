a = [1,2,3]
b = [1,2,3]
c = []

for i in range(len(a)):
    c.append(a[i] * b[i])

for i in c:
    print(i)