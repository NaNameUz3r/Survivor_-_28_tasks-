def WordSearch(len, s, subs):
    
    def find_string_length(string):
        return sum(1 for x in string)

    chunks = iter(s.split())

    lines, current = [], next(chunks)
   
    for i in chunks:
        if find_string_length(current) + 1 + find_string_length(i) > len:
            lines.append(current)
            current = i
        else:
            current += " " + i
    lines.append(current)
    
    if ' ' not in lines[0] and find_string_length(lines[0]) > len:
        lines.append(lines[0][len:])
        lines[0] = lines[0][:len]

    def is_substring(input_arr):
        for j in input_arr.split():
            if j == subs:
                return 1
        return 0
        
    substr_find_bitmap = [is_substring(g) for g in lines]
    
    return substr_find_bitmap


print(WordSearch(12, 'строка разбивается на набор строк через выравнивание по заданной ширине.', 'строк'))
