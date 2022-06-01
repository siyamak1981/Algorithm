"""
[2, 7, 3, 5, 9, 4] , 10 =>[1, 2]

"""

def tow_sum(list, key):
    first = 0
    last = len(list) - 1
    while first <= last:
        result = list[first] + list[last]
        if result == key:
            return(first, last)
        elif result < key:
           first += 1
        else:
            last -= 1

        
print(tow_sum([2, 7, 3, 5, 9, 4], 10))