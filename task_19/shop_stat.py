def ShopOLAP(N, items):

    item_list = items
    item_dict = {}

    for i in item_list:
        if i.split()[0] not in item_dict:
            item_dict[i.split()[0]] = int(i.split()[1])
        else:
            item_dict[i.split()[0]] += int(i.split()[1])

    result = []
    for key, value in sorted(item_dict.items(), key=lambda x: (-x[1], x[0])):

        result.append(key + ' ' + str(value))

    return result

