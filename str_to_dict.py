x = "foo"
y = "bar"
dict = {}
for i in range(len(x)):
    dict[x[i]] = y[i]

print(dict)


x = [1,2,3,4,5,2,1,6,5]
list = ['a', 1 , 'b', 5, 'c', 3, 'd', 99]
def foo(arr):
        it = iter(arr)
        print(dict(zip(it, x)))

foo(list)