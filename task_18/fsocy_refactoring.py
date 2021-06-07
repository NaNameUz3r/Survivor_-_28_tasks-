def MisterRobot(N, data):

    SORTED_DATA = sorted(data)

    def swapper(list_to_swap):
        swap_count = 0
        while not list_to_swap[0] < list_to_swap[1] < list_to_swap[2] and (
                swap_count != 3):
            list_to_swap.append(list_to_swap.pop(0))
            swap_count += 1
        return list_to_swap

    brute_force_success = True

    while brute_force_success:
        brute_force_success = False
        for i in range(len(data) - 2):
            piece_to_swap = data[i:i+3]

            if not piece_to_swap[0] < piece_to_swap[1] < piece_to_swap[2]:
                piece_snapshot = data[i:i+3]
                data[i:i+3] = swapper(piece_to_swap)
                if data[i:i+3] == piece_snapshot:
                    brute_force_success = False
                else:
                    brute_force_success = True

    if data == SORTED_DATA:
        return True
    else:
        return False
