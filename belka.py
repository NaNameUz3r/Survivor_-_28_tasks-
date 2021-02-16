#!/usr/bin/env python3


def squirrel(N):
    
    n_fact = 1
    for i in range(1, N + 1):
        n_fact *= i
    
    first_num = str(n_fact)[:1]
    return int(first_num)
