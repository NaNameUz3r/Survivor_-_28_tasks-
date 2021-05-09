def Keymaker(k):

    doors = [False for i in range(k)]

    for i in range(len(doors)):
        doors[i] = True


    for i in range(1, len(doors), 2):
        doors[i] = False


    for i in range(2, len(doors), 3):
        if doors[i]:
            doors[i] = False
        elif not doors[i]:
            doors[i] = True


    for i in range(3, len(doors)):
        if doors[i]:
            doors[i] = False
        elif not doors[i]:
            doors[i] = True

    result = ''
    for i in doors:
        if i:
            result += '1'
        else:
            result += '0'

    return result


