x  = [{1:2},{3:5}]
y = {}
for i in x:
    for j in i:
        y[j] = i[j]
print(y)
# output
# {1: 2, 3: 5}


# sparate a str with 2 distance in a list
x = "dorodhdt"
y = []

for i in range(0, len(x), 2):
    p = x[i] + x[i + 1]
    y.append(p)
print(y)
  

# median test japan

x = [2,3,4,5,6,7,8,1]
for i in range(len(x)):
    key = x[i]
    y = i - 1
    while  x[y] > key and y >= 0:
        
        x[y + 1] = x[y]
        y = y - 1
    x[y + 1] = key

print(x)
m = len(x)
p = []
if m % 2 == 0:
    u = m // 2
    u = u - 1
    o = u + 1
    for i in x:
        if x[u] in p and x[o] in p:
            pass
        else:
            p.append(x[u])
            p.append(x[o])
s = sum(p)
print(int(s) / 2)