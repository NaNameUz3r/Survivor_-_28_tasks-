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
    for i in range(len(values_list)):
        if values_list[i] == repeats:
            continue
        elif values_list[i] - 1 == repeats and check or (
            values_list[i] - 1 == 0 and check
        ):
            check = False
            continue
        else:
            break
    else:
        return True
    return False

