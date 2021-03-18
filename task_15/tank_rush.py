def TankRush(H1, W1, S1, H2, W2, S2):
    first_map = S1.split()
    second_map = S2.split()

    for i in range(H1):
        if second_map[0] in first_map[i]:
            position = first_map[i].find(second_map[0][0])
            for j in range(H2):
                if second_map[j] in first_map[i + j] and (
                        first_map[i + j].find(second_map[j][0]) == position
                ):
                    continue
                else:
                    break
            else:
                return True

    return False

