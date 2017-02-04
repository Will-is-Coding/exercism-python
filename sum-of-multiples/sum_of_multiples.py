def sum_of_multiples(maxNum, factors):
    multiples = []
    for factor in factors:
        if factor != 0:
            for num in range(factor, maxNum, factor):
                if num not in multiples:
                    multiples.append(num)

    return sum(multiples)