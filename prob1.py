def multiple(max_range):
    multiples = []
    for num in range(max_range):
        if num % 5 == 0 or num % 3 == 0:
            multiples += [num]

    return multiples

print(sum(multiple(1000)))
