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

    larger_number = list(larger[::-1])
    lesser_number = list(lesser[::-1])
    result = []

    for i in range(len(lesser_number)):
        if int(larger_number[i]) == int(lesser_number[i]):
            result.append('0')
        if int(larger_number[i]) > int(lesser_number[i]):
            tmp = int(larger_number[i]) - int(lesser_number[i])
            result.append(str(tmp))
        elif int(larger_number[i]) < int(lesser_number[i]):
            larger_number[i + 1] = str(int(larger[i + 1]) - 1)
            tmp = (int(larger_number[i]) + 10) - int(lesser_number[i])
            result.append(str(tmp))

    if len(result) == 0:
        result.append('0')
    appendix = larger_number[len(lesser_number):]
    result.append(''.join(appendix))
    result_string = ''.join(result)
    result_string = result_string[::-1]
    result_string = str(int(result_string))
    return result_string

