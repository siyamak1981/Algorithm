
def first_accurance(string, key):
    first = 0
    last = len(string) - 1
    while first <= last:
        mid =first +  (last - first) // 2

        if string[mid] < key:
            mid = mid + 1
            first = mid
        elif string[mid] > key:
            mid = mid - 1
            last = mid
        else:
            break
 
    for i in range(len(string)):
        if string[i] == key:
            return i

print(first_accurance([1,2,2,3,3,3,4,5,8,9],3))