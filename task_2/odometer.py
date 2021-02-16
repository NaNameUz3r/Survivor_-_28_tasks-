#!/usr/bin/env python3


def odometer(oksana):

    distance = 0
    speed = 0
    time = 0
    for i in range(len(oksana)):
        if i % 2 == 0:
            speed += oksana[i]
        else:
            time += oksana[i]
    distance = speed * time
    return distance
