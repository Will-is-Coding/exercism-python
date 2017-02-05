def difference(num):
    """Compute the difference of squares for a given number

    Given a num, compute both the square of sum and sum of squares,
    and return the difference

    Arguments:
        num {integer, float} -- Number to compute difference of squares

    Returns:
        integer, float -- Difference of the squares
    """
    return square_of_sum(num) - sum_of_squares(num)


def sum_of_squares(num):
    """Sum of the squares of a number

    Compute the sum of squares given a num
    Ex: 1**2 + 2**2 + ... + 10**2 = 385

    Arguments:
        num {integer, float} -- Number to compute sum of its squares

    Returns:
        integer, float -- Sum of the squares of the number
    """
    sumOfSquares = 0
    for num in range(num + 1):
        sumOfSquares += num**2
    return sumOfSquares


def square_of_sum(num):
    """Square of the sum of a number

    Compute the square of the sum of a number
    Ex: (1 + 2 + ... + 10)**2 = 55**2 = 3025

    Arguments:
        num {integer, float} -- Number to compute square of the sum

    Returns:
        integer, float -- Square of the sum of the number
    """
    return sum(range(num + 1))**2
