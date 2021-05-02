def build_balance(build_variant,
                  open_parentheses,
                  close_parentheses,
                  init_opened_amount,
                  result):

    if open_parentheses == init_opened_amount and (
            close_parentheses == init_opened_amount):
        result.append(build_variant)
    else:
        if open_parentheses < init_opened_amount:
            build_balance(build_variant + '(',
                          open_parentheses + 1,
                          close_parentheses,
                          init_opened_amount,
                          result)
        if close_parentheses < open_parentheses:
            build_balance(build_variant + ')',
                          open_parentheses,
                          close_parentheses + 1,
                          init_opened_amount,
                          result)
    return result


def BalancedParentheses(N):
    result = []
    result = build_balance('', 0, 0, N, result)
    return ' '.join(result)

