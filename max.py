x = [1, 2, 3, 4, 5, 8, 7, 9]
y = 0
for i in range(len(x)):
    while x[y] < x[i]:
        x[y] = x[y + 1]
        y += 1
print(x[y])