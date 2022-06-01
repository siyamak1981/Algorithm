def foo(x):
    list = []
    val = min(x)
    y = x.pop(x.index(val))
    for i in x:
        list.append(i)
    print(list)
foo([5,4,3,6,-2,1,8,0])