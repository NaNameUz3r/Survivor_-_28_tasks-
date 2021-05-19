def BiggerGreater(input):

    def permute(string, permute_start_index, permute_stop_index):
        if permute_start_index == permute_stop_index:
            add_to_results(string)
        else:
            for i in range(permute_start_index, permute_stop_index + 1):
                string[permute_start_index], string[i] = \
                    string[i], string[permute_start_index]

                permute(string, permute_start_index + 1, permute_stop_index)

                string[permute_start_index], string[i] = \
                    string[i], string[permute_start_index]

    def add_to_results(lst):
        permuted_words_list.append(''.join(lst))

    input_string = input
    permuted_words_list = []
    input_length = len(input_string)
    input_lst = list(input_string)

    permute(input_lst, 0, input_length - 1)

    permuted_words_list.sort()

    initial_word_index = permuted_words_list.index(input_string)
    if initial_word_index == len(permuted_words_list) - 1:
        return ''
    elif len(set(permuted_words_list)) == 1:
        return ''
    else:
        return permuted_words_list[initial_word_index + 1]



