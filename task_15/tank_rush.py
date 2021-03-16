def TankRush(H1, W1, S1, H2, W2, S2):

    first_map = S1.split()
    second_map = S2.split()

    result = False
    
    for i in second_map:
        for j in first_map:
            if i in j:
                result = True
                break
    return result

