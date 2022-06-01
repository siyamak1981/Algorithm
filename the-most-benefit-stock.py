

def most_stock(x):
    z = []
    for i in range(1,len(x)):
        p = x[i] - x[i - 1]
        z.append(p)
        if max(z) == p:
            print(x[i])

    for k in range(1, len(x)):
        if max(z) == x[k] - x[k - 1]:
            print(f"the most use full is the:{x[k]}")

most_stock([7,1,5,3,4,6])