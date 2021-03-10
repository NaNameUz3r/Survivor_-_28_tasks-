def Unmanned(L, N, track):

    road_length = L
    abs_time = 0
    moving_time = 0
    time_gap = 0
    while road_length > 0:

        if len(track) == 0:
            break

        if moving_time == track[0][0] and (
                abs_time % (track[0][1] + track[0][2])) < track[0][1]:
            time_diff = track[0][1] - (abs_time % (track[0][1] + track[0][2]))
            time_gap += time_diff
            moving_time += time_diff
            abs_time += time_diff
            if len(track) > 1:
                track[1][0] = track[1][0] + time_gap
            track.pop(0)
            continue
        abs_time += 1
        moving_time += 1
        road_length -= 1

    return moving_time

