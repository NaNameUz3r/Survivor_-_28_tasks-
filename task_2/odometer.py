#!/usr/bin/env python3


def odometer(oksana):

    distance = 0
    speed = 0
    time = 0
    for i in range(len(oksana)):
        if i % 2 == 0:
            speed = oksana[i]
        elif i % 2 != 0 and i == 1:
            time = oksana[i]
            distance += speed * time
        else:
            time = oksana[i]
            distance += speed * (time - oksana[i - 2]) 
    return distance
