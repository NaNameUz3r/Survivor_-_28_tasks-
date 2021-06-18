def PatternUnlock(N, hits):

    line = 1
    diag = (line * line + line * line) ** 0.5

    unlock_dict = {1: {6: line, 2: line, 9: line, 5: diag, 8: diag},
                   2: {1: line, 9: diag, 8: line, 7: diag,
                   3: line, 4: diag, 5: line, 6: diag},
                   3: {2: line, 8: diag, 7: line, 4: line, 5: diag},
                   4: {5: line, 2: diag, 3: line},
                   5: {6: line, 1: diag, 2: line, 3: diag, 4: line},
                   6: {1: line, 2: diag, 5: line},
                   7: {3: line, 2: diag, 8: line},
                   8: {7: line, 3: diag, 2: line, 1: diag, 9: line},
                   9: {8: line, 2: diag, 1: line}
                   }

    line_length = 0
    for i in range(N - 1):
        value = unlock_dict.get(hits[i]).get(hits[i + 1])
        line_length += value

    assert line_length > 0, "line length can not be less than zero"

    line_length = round(line_length, 5)
    line_length = str(line_length)
    zero_stripped_length = []
    for char in line_length:
        if char != '0' and char != '.':
            zero_stripped_length.append(char)

    zero_stripped_length = ''.join(zero_stripped_length)
    
    return zero_stripped_length
