#!/usr/bin/env python3


def squirrel(N):
    
    n_factorial = 1
    for i in range(1, N + 1):
        n_factorial *= i
    
    first_digit = str(n_factorial)[0]
    return int(first_digit)
