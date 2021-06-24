def BiggerGreater(input):

    def permute(list_to_permute, start, end):
        if start == end:
            add_to_results(list_to_permute)
        else:
            for i in range(start, end + 1):
                list_to_permute[start], list_to_permute[i] = \
                    list_to_permute[i], list_to_permute[start]

                permute(list_to_permute, start + 1, end)

                list_to_permute[start], list_to_permute[i] = \
                    list_to_permute[i], list_to_permute[start]

    def add_to_results(char_list):
        permuted_variants.append(''.join(char_list))

    def find_next_mutation(permutations_list):
        permutations_list.sort()

        initial_word_index = permutations_list.index(input)
        if initial_word_index == len(permutations_list) - 1:
            next_permute = ''
        elif len(set(permutations_list)) == 1:
            next_permute = ''
        else:
            next_permute = permutations_list[initial_word_index + 1]

        return next_permute

    LENGTH_OF_STRING = len(input)
    input_word_char_list = list(input)

    permuted_variants = []
    permute(input_word_char_list, 0, LENGTH_OF_STRING - 1)

    next_mutation = find_next_mutation(permuted_variants)
    return next_mutation



print(BiggerGreater("вкиб"))