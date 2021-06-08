def Unmanned(L, N, track):

    road_length = L
    absolute_time = 0
    moving_time = 0
    time_gap = 0
    while road_length > 0:

        if len(track) == 0:
            moving_time += road_length
            break

        is_moving = moving_time == track[0][0]
        time_delta = absolute_time % (track[0][1] + track[0][2])

        if is_moving and time_delta < track[0][1]:
            time_diff = track[0][1] - time_delta
            time_gap += time_diff
            moving_time += time_diff
            absolute_time += time_diff
            if len(track) > 1:
                track[1][0] = track[1][0] + time_gap
            track.pop(0)
            continue
        absolute_time += 1
        moving_time += 1
        road_length -= 1

    return moving_time

