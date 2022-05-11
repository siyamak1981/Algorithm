

def foo(x, key):
    for i in range(len(x)):
        if key == x[i]:
            print(i)
        
    return -1
# print(foo([1,2,3,4,5,2,1], 13))




def foo(x, key):
    first = 0
    last = len(x) - 1
    mid = last // 2
    # mid = 2
    while first <= last:
        if key > x[mid]:
            # 60 > 30
            # 60 > 40
            # 60 > 50
            # ---------------
            
            mid += 1
            # mid = 3
            # mid = 4
            # mid = 5
            # ---------------
         
            first = mid
            # first = 3
            # first = 4
            # first = 5
            # -----------------
     
        else:
            mid -= 1
            # mid = 1
            # mid = 0
            last = mid
            # last = 1
            # last = 0
    print(first)
# foo([10,20,30,40,50], 20)


