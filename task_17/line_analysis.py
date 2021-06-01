def LineAnalysis(line):

    dots_patterns_list = line.split('*')
    if len(dots_patterns_list) > 1:
        dots_patterns_list.pop(0)
        dots_patterns_list.pop(-1)

    unique_dots_patterns = set(dots_patterns_list)

    return not len(unique_dots_patterns) > 1

