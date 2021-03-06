def UFO(N, data, octal):

    converted = []

    if octal:
        for i in range(N):
            result = 0
            power = len(str(data[i])) - 1
            for j in str(data[i]):
                tmp = int(j) * (8 ** power)
                result += tmp
                power -= 1
            converted.append(result)
    else:
        for i in range(N):
            result = 0
            power = len(str(data[i])) - 1
            for j in str(data[i]):
                tmp = int(j) * (16 ** power)
                result += tmp
                power -= 1
            converted.append(result)
    
    return converted

