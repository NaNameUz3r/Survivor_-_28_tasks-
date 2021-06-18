def BigMinus(s1, s2):

    larger_number = ''
    lesser_number = ''

    if len(s1) == len(s2):
        for i in range(len(s1)):
            if int(s1[i]) > int(s2[i]):
                larger_number = s1
                lesser_number = s2
            elif int(s1[i]) < int(s2[i]):
                larger_number = s2
                lesser_number = s1

    elif len(s1) > len(s2):
        larger_number = s1
        lesser_number = s2
    else:
        larger_number = s2
        lesser_number = s1

    larger_number = list(larger_number[::-1])
    lesser_number = list(lesser_number[::-1])
    calculation_result = []

    for i in range(len(lesser_number)):
        if int(larger_number[i]) == int(lesser_number[i]):
            calculation_result.append('0')
        if int(larger_number[i]) > int(lesser_number[i]):
            digit_to_ascribe = int(larger_number[i]) - int(lesser_number[i])
            calculation_result.append(str(digit_to_ascribe))
        elif int(larger_number[i]) < int(lesser_number[i]):
            larger_number[i + 1] = str(int(larger[i + 1]) - 1)
            digit_to_ascribe = (int(larger_number[i]) + 10) - (
                                int(lesser_number[i]))
            calculation_result.append(str(digit_to_ascribe))

    digit_to_ascribe = "!error!"

    if len(calculation_result) == 0:
        calculation_result.append('0')
    appendix = larger_number[len(lesser_number):]
    calculation_result.append(''.join(appendix))
    appendix = "!error!"
    calculation_result = ''.join(calculation_result)
    calculation_result = calculation_result[::-1]
    return calculation_result


print(type(BigMinus("1", "321")))
print((BigMinus("1", "321")))
