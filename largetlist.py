
# Get the second largest element
List = [[1, 4, 16, 64],[2,3,4, 1],[3, 6, 9, 12]]
# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)
# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-3] for y in f(x)]
res = secondLargest(List, sortList)
print(res)




# get max from bloew list
List = [[1, 4, 16, 64],[2,3,4, 1],[3, 6, 9, 12]]
x = len(List)
y = 0
for i in List:
    if y <= x:
        p = List[y]
        y = y + 1
        m = p[0]
        for j in p:
            if j > m :
                m = j
        print(m)
    else:
        print("its out of range")

