l = [5,3,4,6,1,2]


# rottate 2 number of list to end of it
def leftRotate(arr, d, n):
    for i in range(d):
        temp = arr[0]
        # temp = 1 , 2
        for j in range(n - 1):
            # print(arr[j])
            # 1 2 3 4 5 6
            # 2 3 4 5 6 7
            # j => 
            # 0 1 2 3 4 5
            # 0 1 2 3 4 5
            # arr[j + 1]
            # 2 3 4 5 6 7  
            # 3 4 5 6 7 1
            arr[j] = arr[j + 1]
            # print(arr[j])
            # [2 3 4 5 6 7]
            # [3 4 5 6 7 1]
            # -----------------
        arr[n - 1] = temp
        # arr[6] = 1 2 
        # print(arr)
        # [2, 3, 4, 5, 6, 7, 1]
        # [3, 4, 5, 6, 7, 1, 2]
    # print(arr)
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)


x = [1,2,3,4,5,6,7]
d = 2
n = 7
for i in range(d):
    temp = x[i]
    # print(temp)
    for j in range(n - 1):
        x[j] = x[j + 1]
    #    23456
    #    34566
    x[n - 1] = temp
print(x)
         

def leftRotate(arr, d, n):
    d = d % n
    for i in range(2, n):
        # move i-th values of blocks
        temp = arr[i]
        # 3 6 2 5 1
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
    print(arr)
# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
leftRotate(arr, d, n)
# ---------------------------------------------------


def foo(x,k):
    list = []
    list =x[:k] + x[k:]
    return(list)
print(foo([1,2,3,4,5,6,7], 2))
# -------------------------------------------------------
x = [1,2,3,4,5,6,7]
k = 2
y  = x[:k]
z = []
for i in range(2, len(x)):
    z.append(x[i])
print(z + y)