#!/usr/bin/env python3

def odometer(oksana):

    total_distance = 0
    current_speed = 0
    trip_time = 0
    for i in range(len(oksana)):
        if i % 2 == 0:
            current_speed = oksana[i]
        elif i % 2 != 0 and i == 1:
            trip_time = oksana[i]
            total_distance += current_speed * trip_time
        else:
            trip_time = oksana[i]
            total_distance += current_speed * (trip_time - oksana[i - 2]) 
    return total_distance
