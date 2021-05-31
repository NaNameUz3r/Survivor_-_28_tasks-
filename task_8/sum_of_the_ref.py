#!/usr/bin/env python3

def SumOfThe(N, data):

    for i in range(N):
        data_copy_to_process = data.copy()
        sum_candidate = data_copy_to_process.pop(i)
        if sum(data_copy_to_process) == sum_candidate:
            return sum_candidate

