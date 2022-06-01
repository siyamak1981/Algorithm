# change list to dict
x = [1,2,3,4,5,2,1,6,5]
print({i : x[i] for i in range(len(x))})


# change list to dict with zip
list = ['a', 1 , 'b', 5, 'c', 3, 'd', 99]
def foo(arr):
        it = iter(arr)
        print(dict(zip(it, x)))

foo(list)

# arangment in dict
# c = {'a':55, 'b':2, 'g':3, 'c': 4, 'c':4,'g':5, 'a':1}
# print(c)

x = ['a','b','c','b','d','m','n','n', 'n']
y = range(len(x))
dict = {}
for i in range(len(x)):
        dict[y[i]] = x[i]
print(dict)
 