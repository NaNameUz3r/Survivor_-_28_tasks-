def TreeOfLife(H, W, N, tree):

    start_list = []
    for row in tree:
        start_list.append(list(row))

    work_list = []

    # создадим рабочий трехмерный массив, где в "ветках" первый элемент - возраст ветки
    # а второй элемент признак на её уничтожение

    for i in range(len(start_list)):
        work_list.append([])
        for j in range(len(start_list[i])):
            if start_list[i][j] == '.':
                work_list[i].append([0, 0])
            elif start_list[i][j] == '+':
                work_list[i].append([1, 0])

    for year in range(2, N + 2):
        for row in work_list:
            for item in row:
                item[0] += 1

        # проврим наше дерево на предмет старых веток и назначим "признак уничтожения"
        for i in range(len(work_list)):
            for j in range(len(work_list[i])):
                if work_list[i][j][0] >= 3:
                    work_list[i][j][1] = 1
                    if j > 0:
                        work_list[i][j - 1][1] = 1
                    if j < W - 1:
                        work_list[i][j + 1][1] = 1
                    if i > 0:
                        work_list[i - 1][j][1] = 1
                    if i < H - 1:
                        work_list[i + 1][j][1] = 1

        if year % 2 != 0:
            for i in range(len(work_list)):
                for j in range(len(work_list[i])):
                    if work_list[i][j][1] == 1:
                        work_list[i][j][0] = 0
                        work_list[i][j][1] = 0

        # соберем массив в соответствии формату требуемому на выходе

    result_list = []
    for i in range(len(work_list)):
        result_list.append([])
        for item in work_list[i]:
            if item[0] == 0:
                result_list[i].append('.')
            else:
                result_list[i].append('+')

    for i in range(len(result_list)):
        result_list[i] = ''.join(result_list[i])

    return result_list

