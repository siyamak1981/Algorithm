x = [1,2,3,4,5]

def foo(list, max = None, min = None):
    l = []
    if min:
        for i in x:
            if i >= min:
                l.append(i)
                
    if max:
        for i in x:
            if i <= max:
                l.append(i)
                
    print(l)
foo(x, max = 3, min = 3)



    
def foo(list, max = None, min = None):
    min_val = lambda i : True if min is None else (min <= i)
    max_val = lambda i : True if max is None else (max >= i)
    print ([i for i in list if (min_val(i)) and max_val(i)])
foo([1,2,3,4,5,6], max = 3, min = 3)

# 