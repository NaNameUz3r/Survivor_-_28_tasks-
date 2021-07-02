def SherlockValidString(s):

    letters_dict = {}

    for letter in s:
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1

    sorted_dict = {}
    sorted_keys = sorted(letters_dict, key=letters_dict.get)
    for item in sorted_keys:
        sorted_dict[item] = letters_dict[item]

    values_list = list(sorted_dict.values())

    repeats = max(values_list, key=values_list.count)

    check = True
    for item in values_list:
        if item == repeats:
            continue
        elif item - 1 == repeats and check or (
            item - 1 == 0 and check
        ):
            check = False
            continue
        else:
            break
    else:
        return True
    return False
