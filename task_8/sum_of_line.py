#!/usr/bin/env python3


def SumOfLine(N, data):

    for i in range(N):
        temp_data = data.copy()
        scope = temp_data.pop(i)
        if sum(temp_data) == scope:
            return scope
