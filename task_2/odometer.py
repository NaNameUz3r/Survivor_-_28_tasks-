#!/usr/bin/env python3


def odometer(oksana):

    distance = 0
    for i in range(0, len(oksana), 2):
        print(oksana[i])
        distance += oksana[i]
    return distance
