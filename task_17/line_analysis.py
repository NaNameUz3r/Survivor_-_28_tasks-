def LineAnalysis(line):

    lst = line.split('*')
    if len(lst) > 1:
        lst.pop(0)
        lst.pop(-1)

    lst_set = set(lst)

    return not len(lst_set) > 1

