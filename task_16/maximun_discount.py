def MaximumDiscount(N, price):

    goods_prices_list = sorted(price, reverse=True)

    fool_discount = sum(goods_prices_list[::-1][:N // 3])
    smart_discount = sum(goods_prices_list[2::3])

    return max([fool_discount, smart_discount])

