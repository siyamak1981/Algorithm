def bead_sort(sequence):
    if any(not isinstance(i, int) or i < 0 for i in sequence):
        return TypeError("sequence must be greate than 0 or be integer")

    for _ in range(len(sequence)):
        for i,(rod_upper, rod_lower) in enumerate(zip(sequence,sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower
    return sequence

print(bead_sort([4,7,2,9,3,6,7]))


