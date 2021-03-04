def BigMinus(s1, s2):

    larger = ''
    lesser = ''

    if len(s1) == len(s2):
        for i in range(len(s1)):
            if int(s1[i]) > int(s2[i]):
                larger = s1
                lesser = s2
            elif int(s1[i]) < int(s2[i]):
                larger = s2
                lesser = s1

    elif len(s1) > len(s2):
        larger = s1
        lesser = s2
    else:
        larger = s2
        lesser = s1

    larger = list(larger[::-1])
    lesser = list(lesser[::-1])
    result = []

    for i in range(len(lesser)):
        if int(larger[i]) == int(lesser[i]):
            result.append('0')
        if int(larger[i]) > int(lesser[i]):
            tmp = int(larger[i]) - int(lesser[i])
            result.append(str(tmp))
        elif int(larger[i]) < int(lesser[i]):
            larger[i + 1] = str(int(larger[i + 1]) - 1)
            tmp = (int(larger[i]) + 10) - int(lesser[i])
            result.append(str(tmp))

    appendix = larger[len(lesser):]
    result.append(''.join(appendix))
    result_string = ''.join(result)
    result_string = result_string[::-1]

    return result_string

