def TankRush(H1, W1, S1, H2, W2, S2):

    field = S1.split()
    to_find = S2.split()

    global_match_flag = False

    for window_y in range(len(field) - len(to_find) + 1):

        if global_match_flag:
            break

        for window_x in range(len(field[0]) - len(to_find[0]) + 1):
            match_flag = True
            for find_y in range(len(to_find)):
                for find_x in range(len(to_find[0])):
                    if field[window_y + find_y][window_x + find_x] != to_find[find_y][find_x]:
                        match_flag = False

            if match_flag:
                global_match_flag = True
                break

    return global_match_flag

