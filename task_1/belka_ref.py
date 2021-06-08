import math


def squirrel(N):
    
    n_factorial = 1
    for i in range(1, N + 1):
        n_factorial *= i

    first_digit = get_first_digit(n_factorial)
    return first_digit


def get_first_digit(number):
    return number // 10 ** (int(math.log(number, 10)))
