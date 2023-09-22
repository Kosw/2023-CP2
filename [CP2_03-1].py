x = int(input())
y = int(input())

l1 = []
l2 = []

for i in range(x):
    l1.append(i)

for j in range(y):
    l2.append(j)

l1.extend(l2)
print(l1)