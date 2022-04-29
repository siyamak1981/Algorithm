
# l = [5,3,4,6,1,2]

# "sort a list without less to greate"
# for i in range(len(l)):
#     # i = 0,1,2,3,4,5
#     x = l[i] # 5 3 4 6 1 2
#     y = i - 1 # -1,0,1,2,3,4
#     # l[y] = 2,5,3,4,6,1
#     while  l[y] > x and y >= 0:
#          # 2 > 5 and -1 >= 0
#          # 5 > 3 and 0 >= 0
#         #  3 > 4 and 1 >=0
#          # 6 > 1 and 3 >= 0
#         l[y + 1] = l[y]
#         y = y - 1
#     l[y + 1] = x
#     # l[0] = 5

# print(l)


# x = True
# while x:
#     x = False
#     for i in range(len(l)-1):
#             if l[i] > l[i + 1]:
#                 l[i], l[i+1] = l[i+1], l[i]
#                 x = True
# print(l)


# for i in range(len(l)):
#     y = i
#     for j in range(i + 1, len(l)):
#         print(j)
#         if l[j] < l[y]:
#             y = j
#     l[i], l[y] = l[y], l[i]
# print(l)


# i = 0            # first item
# j = len(l)-1   # last item
# while i<j:
#     l[i],l[j] = l[j],l[i]
#     i += 1
#     j -= 1
# print(l)

