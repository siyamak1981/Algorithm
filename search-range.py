
"""binary search"""

def search_range(list, key):
    first = 0
    last = len(list) - 1
    while first <= last:
        mid =first +  (last - first) // 2
        if key < list[mid]:
            mid -= 1
            last = mid
        elif key > list[mid]:
            mid += 1
            first = mid
        else:
            break 

    for i in range(len(list) -1, -1, -1):
        if list[i] == key:
            return [mid, i]
    return [None, None]

print(search_range([5,6,7,7,8,8,8,9,9,10],55))

