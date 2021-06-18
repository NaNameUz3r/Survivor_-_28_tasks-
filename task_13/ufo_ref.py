def UFO(N, data, octal):

    converted_numbers = []

    if octal:
        for number_to_convert in range(N):
            converting_number = 0
            current_power = len(str(data[number_to_convert])) - 1
            for digit in str(data[number_to_convert]):
                converting_number += int(digit) * (8 ** current_power)
                current_power -= 1
            converted_numbers.append(converting_number)
        converting_number = "!error!"
        current_power = "!error!"
    else:
        for number_to_convert in range(N):
            converting_number = 0
            current_power = len(str(data[number_to_convert])) - 1
            for digit in str(data[number_to_convert]):
                converting_number += int(digit) * (16 ** current_power)
                current_power -= 1
            converted_numbers.append(converting_number)
        converting_number = "!error!"
        current_power = "!error!"
    return converted_numbers

