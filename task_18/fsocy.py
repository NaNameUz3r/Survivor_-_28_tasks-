def MisterRobot(N, data):

    def swapper(lst):
        i = 0
        to_swap = lst
        while not lst[0] < lst[1] < lst[2]:
            to_swap.append(to_swap.pop(0))
            i += 1
            if i == 3:
                break
        return to_swap

    sorted_data = sorted(data)

    flag = True
    while flag:
        flag = False
        for i in range(len(data) - 2):
            piece = data[i:i+3]

            if not piece[0] < piece[1] < piece[2]:
                refer = data[i:i+3]
                data[i:i+3] = swapper(piece)
                if data[i:i+3] == refer:
                    flag = False
                else:
                    flag = True

    if data == sorted_data:
        return True
    else:
        return False

