
# You a given a number N. You need to print the pattern for the given value of N.
# for N = 2 the pattern will be 
# 2 2 1 1
# 2 1
# for N = 3 the pattern will be 
# 3 3 3 2 2 2 1 1 1
# 3 3 2 2 1 1
# 3 2 1

# Example 1:

# Input: 2
# Output:
# 2 2 1 1 $2 1 $

# Example 2:

# Input: 3
# Output:
# 3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $




def printPat(n):
    c = n
    s = ''
    for i in range(n):
        for j in range(n,0,-1):
            for k in range(c):
                s += str(j) + ' '
        s += '$'
        c -= 1
    return s

if __name__=='__main__':
    t=int(input("what is your number?\n"))
    for i in range(t):
        n= int(input("again what is your number?\n"))

        print (printPat(n))
