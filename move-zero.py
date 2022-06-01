def move_zero(x):
    list = []
    zeros = 0
    for i in x:
        if i == 0 and type(i) != bool:
            zeros += 1
            print(zeros)
        else:
            list.append(i)
    list.extend([0] * zeros)
    print(list)
move_zero([False, 1, 2 ,0 ,6 ,0, 8, "a", 9])


# --------------------------------------------------


def move_zero(x):
    list = []
    zeros = 0
    z = []
    for i in x:
        if i == 0 and type(i) != bool:
            z.append(i)
        else:
            list.append(i)

    list.extend(z)
    print(list)
move_zero([False, 1, 2 ,0 ,6 ,0, 8, "a", 9])

