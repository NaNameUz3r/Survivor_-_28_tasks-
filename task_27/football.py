def first_coaching_reception(input_lst):
    sorted_input = sorted(input_lst)
    list_length = len(input_lst)

    for i in range(list_length):
        for j in range(i + 1, list_length):
            input_lst[i], input_lst[j] = input_lst[j], input_lst[i]
            if sorted_input == input_lst:
                return True
            else:
                input_lst[i], input_lst[j] = input_lst[j], input_lst[i]
    return False


def second_coaching_reception(input_lst):
    results_local = [input_lst[::-1]]
    for i in range(1, len(input_lst)):
        for j in range(i + 2, len(input_lst) + 1):
            new_chunk = input_lst[:i] + input_lst[i:j][::-1] + input_lst[j:len(input_lst)]
            results_local.append(new_chunk)

    return sorted(input_lst) in results_local


def Football(F, N):

    return first_coaching_reception(F) or \
           second_coaching_reception(F)

