
x = [2,3,4,5,6,7,8,1]
"""sorted list and devided and get a number before and after devide number and then sum and devide"""
# start sort list
for i in range(len(x)):
    key = x[i]
    y = i - 1
    while  x[y] > key and y >= 0:
        x[y + 1] = x[y]
        y = y - 1
    x[y + 1] = key
# end sorted list
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


# ------------------------------------------
"""separate to tow list and get max and min of list1 and list 2 and then devided"""
list_last= []
list_first= []
mid = len(x) // 2
x = sorted(x)
for i in range(len(x)):
        if i < mid:
            list_first.append(x[i])
        if i >= mid:
         list_last.append(x[i])
print((max(list_first) +  min(list_last))/ 2)
