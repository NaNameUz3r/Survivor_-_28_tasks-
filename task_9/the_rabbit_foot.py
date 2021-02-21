#!/usr/bin/env python3


def TheRabbitFoot(s, encode):

    # вырезаю пробелы
    s = s.replace(' ', '')

    # считаю длинну строки, после чего вычисляю её квадратный корень
    s_length = len(s)
    s_sqrt = round((s_length ** 0.5), 2)
    print(s_length, s_sqrt)

    # получаем верхнюю и нижнюю границы корня, пишем их в отдельные переменные
    # как значения колва строк и колонок
    matrix_rows  = int(s_sqrt // 1)
    matrix_cols = int(str(s_sqrt)[2:3])
   
    # наращиваем колво строк, если длинна не влезает в произведение эллементов строк*столбцов
    while matrix_rows * matrix_cols < s_length:
        matrix_rows += 1
    print(matrix_rows, matrix_cols)
    
    
    decipher = []

    while len(s) > matrix_cols:
        decipher.append(list(s[:matrix_cols]))
        s = s[matrix_cols:]
    else:
        decipher.append(list(s))
        
    result = []
         
    for i in range(matrix_cols):
        for j in range(matrix_rows):
            if i < len(decipher[j]):
                result.append(decipher[j][i])
        result.append(' ')
                
    result = ''.join(result).strip()
    
    print(result)






TheRabbitFoot('отдай мою кроличью лапку', True)
