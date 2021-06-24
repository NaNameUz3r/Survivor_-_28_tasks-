def ShopOLAP(N, items):

    def build_sales_dict(items_list):
        sales_stat_container = {}

        for item in items_list:

            item_name = item.split()[0]
            sales_count = int(item.split()[1])

            if item_name not in sales_stat_container:
                sales_stat_container[item_name] = sales_count
            else:
                sales_stat_container[item_name] += sales_count
        return sales_stat_container

    def sort_sales(dict_to_sort):
        sorted_sales_list = []
        for key, value in sorted(dict_to_sort.items(),
                                 key=lambda x: (-x[1], x[0])):
            sorted_sales_list.append(key + ' ' + str(value))

        return sorted_sales_list

    sales_dict = build_sales_dict(items)
    sorted_sales = sort_sales(sales_dict)
    return sorted_sales

