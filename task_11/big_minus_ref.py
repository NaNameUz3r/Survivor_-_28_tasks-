def BigMinus(s1, s2):

    def calculate_difference(lesser, bigger):
        calculation_result = []

        for i in range(len(lesser)):
            if int(bigger[i]) == int(lesser[i]):
                calculation_result.append('0')
            if int(bigger[i]) > int(lesser[i]):
                digit_to_ascribe = int(bigger[i]) - int(lesser[i])
                calculation_result.append(str(digit_to_ascribe))
            elif int(bigger[i]) < int(lesser[i]):
                bigger[i + 1] = str(int(larger[i + 1]) - 1)
                digit_to_ascribe = (int(bigger[i]) + 10) - (
                    int(lesser[i]))
                calculation_result.append(str(digit_to_ascribe))

        digit_to_ascribe = "!error!"

        if len(calculation_result) == 0:
            calculation_result.append('0')
        appendix = bigger[len(lesser):]
        calculation_result.append(''.join(appendix))
        appendix = "!error!"
        calculation_result = ''.join(calculation_result)
        calculation_result = calculation_result[::-1]
        return calculation_result

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

    difference = calculate_difference(lesser_number, larger_number)
    return difference
