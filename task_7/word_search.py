#!/usr/bin/env python3



def WordSearch(len, s, subs):

    def lenn(inp_str):
        result = sum(1 for x in inp_str)
        return result
    
    chunks = s.split()
    new_chunks = []

    counter = 0
    words = True 

    while words:
        for i in range(len):
            if s[i] == ' ':
                new_chunks.append(s[:i])
                s = s[i:]
            break
    print(s[:12])
    print(s[6:])
    

WordSearch(12, 'строка разбивается на набор строк через выравнивание по заданной ширине.', 'строк')


