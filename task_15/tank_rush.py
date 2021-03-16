def TankRush(H1, W1, S1, H2, W2, S2):
    first_map = S1.split()
    second_map = S2.split()

    result = False
    founding = []
    for i in second_map:
        for j in first_map:
            if i in j:
                founding.append(j.find(i[0]))

    for g in range(len(founding) - 1):
        if founding[g] == founding[g + 1]:
            result = True
            break
    return result

