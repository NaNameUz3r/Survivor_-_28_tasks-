def MaximumDiscount(N, price):

    goods = sorted(price, reverse=True)

    fool_discount = sum(goods[::-1][:N // 3])
    smart_discount = sum(goods[2::3])

    return max([fool_discount, smart_discount])

