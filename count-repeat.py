# display item without repeat in a list
x = [1,277,1,4,1,5,3,4,3,2,1]
list = []
for i in x:
    if i not in list:
        list.append(i)
    else:
        continue
print(list)
  
#   ------------------------
# to get repeat item
m = []
h = []
for i in x:
    if i in list:
        # print(i, end=',')
        m.append(i)
    else:
        list.append(i)
for j in m:
    if j not in h:
        h.append(j)
    else:
        continue
print(list)
print(h)

# -----------------------------------------------

some_list=['a','b','c','b','d','m','n','n', 'n']

my_list=sorted(some_list)
 
duplicates=[]
for i in my_list:
     if my_list.count(i)>1:
         if i not in duplicates:
             duplicates.append(i)
 
print(duplicates)    

# ---------------------------------------------------
# how to get max duplicate in list
values = {}
for i in some_list:
    if i in values:
       values[i] +=1
    else:
        values[i] = 1
lili = []
max_val = max(values.values())
for i in values.keys():
    if values[i] == max_val:
        lili.append(i)
print(lili)