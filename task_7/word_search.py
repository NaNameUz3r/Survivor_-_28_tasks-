#!/usr/bin/env python3


def WordSearch(len, s, subs):
    
    def lenn(string):
        result = sum(1 for x in string)
        return result
        
        
    chunks = iter(s.split())
    
    print(chunks)
    
    lines, current = [], next(chunks)
   
    for i in chunks:
        if lenn(current) + 1 + lenn(i) > len:
            lines.append(current)
            current = i
        else:
            current += " " + i
    lines.append(current)
    
    if ' ' not in lines[0] and lenn(lines[0]) > len:
        lines.append(lines[0][len:])
        lines[0] = lines[0][:len]

    def check(input_arr):
        for j in input_arr.split():
            if j == subs:
                return 1
        return 0
        
    result = [check(g) for g in lines]
    
    return result
