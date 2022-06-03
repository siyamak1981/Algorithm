def findFrequency (x):
    dict = {}
    for i in range(len(x)):
        if x[i] not in dict:
            dict[x[i]] = 1
        else:
            dict[x[i]] += 1
    print(dict)
            

findFrequency([10, 20, 20, 10, 10, 20, 5, 20])
