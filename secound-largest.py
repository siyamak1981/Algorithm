# arr = [2,5,4,6,3,7]

# def foo(arr):
#    maxi = 0
    # arr.sort()

    # list = []
    # if len(set(arr)) == 1:
    #     return -1
    # for i in range(len(arr)):
    #     if arr[i] >= maxi:
    #         maxi = arr[i]
        
    # for j in range(len(arr)):
    #     if arr[j] != maxi:
    #         list.append(arr[j])
    
    # maxim =0
    # for k in range(len(list)):
    #     if list[k] > maxim:
    #         maxim = list[k]
    # return(maxim)
# print(foo(arr))

def print2largest(self,arr, n):
         first = second = -2147483648
         for i in range(n):
             if (arr[i] > first): 
                 second = first 
                 first = arr[i] 
             elif (arr[i] > second and arr[i] != first): 
                second = arr[i] 
         if (second == -2147483648): 
             return -1
         else: 
             return second
                
