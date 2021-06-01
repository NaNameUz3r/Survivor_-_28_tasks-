def ShopOLAP(N, items):

    items_list = items
    sales_stat_container = {}

    for item in items_list:

        item_name = item.split()[0]
        sales_count = int(item.split()[1])

        if item_name not in sales_stat_container:
            sales_stat_container[item_name] = sales_count
        else:
            sales_stat_container[item_name] += sales_count

    sorted_sales_stat = []
    for key, value in sorted(sales_stat_container.items(),
                             key=lambda x: (-x[1], x[0])):

        sorted_sales_stat.append(key + ' ' + str(value))

    return sorted_sales_stat

