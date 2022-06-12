
def last_accurance(string, key):
    first = 0
    last = len(string) - 1
    
    while first <= last:
        mid =first + (last - first) // 2
        if (string[mid] == key and string[mid] == last) or \
                (string[mid] == key and string[mid + 1] > key):
            return(mid)

        elif (key >= string[mid]):
            mid += 1
            first = mid
     
        else:
            mid -= 1
            last = mid
         
    print(first)

print(last_accurance([1,2,2,3,3,3,4,4,5,6],31))



def foo(x, key):
    count = 0
    for i in range(len(x)):
        if x[i]<= key:
            count += 1
    return count
print(foo([1,2,3,4,6,8,10], 7))