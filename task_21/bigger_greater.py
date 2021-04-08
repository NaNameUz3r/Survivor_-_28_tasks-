def BiggerGreater(input):

    def add_to_results(lst):
        results.append(''.join(lst))

    def permute(string, start, end):
        if start == end:
            add_to_results(string)
        else:
            for i in range(start, end + 1):
                string[start], string[i] = string[i], string[start]
                permute(string, start + 1, end)
                string[start], string[i] = string[i], string[start]

    input_string = input
    results = []
    input_length = len(input_string)
    input_lst = list(input_string)

    permute(input_lst, 0, input_length - 1)

    results.sort()

    input_idx = results.index(input_string)
    if input_idx == len(results) - 1:
        return ''
    elif len(set(results)) == 1:
        return ''
    else:
        return results[input_idx + 1]

