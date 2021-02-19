#!/usr/bin/env python3


def WordSearch(len, s, subs):
    
    def lenn(string):
        result = sum(1 for x in string)
        return result
        
        
    chunks = iter(s.split())
    
    lines, current = [], next(chunks)
    for i in chunks:
        if lenn(current) + 1 + lenn(i) > len:
            lines.append(current)
            current = i
        else:
            current += " " + i
    lines.append(current)
    
    result = []
    
    def check(input_arr):
        for j in input_arr.split():
            if j == subs:
                return 1
        return 0
        
    result = [check(g) for g in lines]
    
    return result
