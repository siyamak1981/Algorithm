# def subString(Str,n):    
#     for Len in range(1,n + 1):
#         for i in range(n - Len + 1):
#             j = i + Len - 1
#             for k in range(i,j + 1):
#                 print(Str[k],end="")
#             print()
# Str = "abcd"
# subString(Str,len(Str))
# --------------------------------------------------
x = "abs"
# for i in range(len(x)):
#     for j in range(i + 1, len(x) + 1):
#         print(x[i: j])


# ------------------------------------------------

for i in range(len(x)):
    temp = ""
    for j in range(i, len(x)):
        temp += x[j]
        print(temp)