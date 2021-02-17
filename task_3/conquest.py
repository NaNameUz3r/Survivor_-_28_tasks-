#!/usr/bin/env python3

def ConquestCampaign(N, M, L, battalion):

    capture_area = []
    for i in range(N):
        capture_area.append([])
        for j in range(M):
            capture_area[i].append(0)

    not_captured = True
    
    day_counter = 1


    for troop in range(0, len(battalion), 2):
        capture_area[battalion[troop] - 1][battalion[troop + 1] - 1] = day_counter 


    for row in capture_area:
        print(*row)
    print('------------')
    print(day_counter, 'day')
    


    for i in range(N):
        for j in range(M):
            if capture_area[i][j] == day_counter:
                if j - 1 >= 0 and capture_area[i][j - 1] < day_counter:
                    capture_area[i][j - 1] = day_counter + 1
                if j + 1 <= M - 1 and capture_area[i][j + 1] < day_counter:
                    capture_area[i][j + 1] = day_counter + 1
                if i - 1 >= 0 and capture_area[i - 1][j] < day_counter:
                    capture_area[i - 1][j] = day_counter + 1
                if i + 1 <= N - 1 and capture_area[i + 1][j] < day_counter:
                    capture_area[i + 1][j] = day_counter + 1
    
    day_counter += 1
    
    
    for row in capture_area:
        print(*row)
    print('------------')
    print(day_counter, 'day')
    




ConquestCampaign(3, 4, 2, [2,2, 3,4])
