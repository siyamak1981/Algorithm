x = ["John", "Paul", "Ringo", "George"]



x = [f"sir {i}" for i in x]
print(x)
# output
# ['sir John', 'sir Paul', 'sir Ringo', 'sir George']



y = []
for i in x:
    y.append(f"sir{i}")
print(y)
# output
# ['sir John', 'sir Paul', 'sir Ringo', 'sir George']