def UFO(N, data, octal):

    converted_numbers = []

    if octal:
        for i in range(N):
            converting_number = 0
            current_power = len(str(data[i])) - 1
            for j in str(data[i]):
                converting_number += int(j) * (8 ** current_power)
                current_power -= 1
            converted.append(converting_number)
    else:
        for i in range(N):
            converting_number = 0
            current_power = len(str(data[i])) - 1
            for j in str(data[i]):
                converting_number += int(j) * (16 ** current_power)
                current_power -= 1
            converted.append(converting_number)
    
    return converted_numbers

