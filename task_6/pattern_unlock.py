#!/usr/bin/env python3


def PatternUnlock(N, hits):

    line = 1
    diag = (line * line + line * line) ** 0.5

    unlock_d = {1: {6: line, 2: line, 9: line, 5: diag, 8: diag},
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

    summary = 0

    for i in range(N - 1):
        value = unlock_d.get(hits[i]).get(hits[i + 1])
        summary += value
    
    summary = round(summary, 5)
    summary = str(summary) 
    result = []
    for char in summary:
        if char != '0' and char != '.':
            result.append(char)

    result = ''.join(result)
    
    return result
