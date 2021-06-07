def TankRush(H1, W1, S1, H2, W2, S2):

    GLOBAL_FIELD = S1.split()
    TAGRET_FIELD = S2.split()

    global_found = False

    for window_y in range(len(GLOBAL_FIELD) - len(TAGRET_FIELD) + 1):

        if global_found:
            break

        for window_x in range(len(GLOBAL_FIELD[0]) - len(TAGRET_FIELD[0]) + 1):
            found = True
            for find_y in range(len(TAGRET_FIELD)):
                for find_x in range(len(TAGRET_FIELD[0])):
                    if GLOBAL_FIELD[window_y + find_y][window_x + find_x] != TAGRET_FIELD[find_y][find_x]:
                        found = False

            if match_flag:
                global_found = True
                break

    return global_found

