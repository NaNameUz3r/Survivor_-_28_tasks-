def Keymaker(k):

    doors = [False for i in range(k)]

    for i in range(len(doors)):
        doors[i] = True

    for i in range(1, len(doors), 2):
        doors[i] = False

    step = 0
    for _ in range(2, k):
        for i in range(2 + step, len(doors), 3 + step):
            if doors[i]:
                doors[i] = False
            elif not doors[i]:
                doors[i] = True
        step += 1


    result = ''
    for i in doors:
        if i:
            result += '1'
        else:
            result += '0'

    return result


