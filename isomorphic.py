""" 
    is isomorphic
    foo, bar => False
    foo , bee =>True
    fow, bee => False

"""

def is_isomorphic(x, y):

    if len(x) != len(y):
        return False
    else:
        dict = {}
        set_values = set()
        for i in range(len(x)):
            if x[i] not in dict:
                if y[i] in set_values:
                    return(False)
                dict[(x[i])] = y[i]
                set_values.add(y[i])
                
            else:
                if dict[(x[i])] != y[i]:
                    return(False)
                
        # return(dict, set_values)
        return(True)


print(is_isomorphic("paper", "title"))