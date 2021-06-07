def BiggerGreater(input):

    def add_to_results(lst):
        permuted_variants.append(''.join(lst))

    def permute(string, start, end):
        if start == end:
            add_to_results(string)
        else:
            for i in range(start, end + 1):
                string[start], string[i] = string[i], string[start]
                permute(string, start + 1, end)
                string[start], string[i] = string[i], string[start]

    LENGTH_OF_STRING = len(input)
    input_word_char_list = list(input)
    permuted_variants = []
    
    permute(input_word_char_list, 0, LENGTH_OF_STRING - 1)

    permuted_variants.sort()

    initial_word_index = permuted_variants.index(input)

    if initial_word_index == len(permuted_variants) - 1:
        next_permute = ''
    elif len(set(permuted_variants)) == 1:
        next_permute = ''
    else:
        next_permute = permuted_variants[initial_word_index + 1]

    return next_permute
