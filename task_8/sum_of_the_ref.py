#!/usr/bin/env python3


def SumOfThe(N, data):

    for i in range(N):
        sum_candidate = temp_data[i]
        if sum(data) == sum_candidate:
            return sum_candidate
