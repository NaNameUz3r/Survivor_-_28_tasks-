def build_balance(build_variant,
                  open_parentheses,
                  close_parentheses,
                  init_opened_amount,
                  current_results_list):

    if open_parentheses == init_opened_amount and (
            close_parentheses == init_opened_amount):
        current_results_list.append(build_variant)
    else:
        if open_parentheses < init_opened_amount:
            build_balance(build_variant + '(',
                          open_parentheses + 1,
                          close_parentheses,
                          init_opened_amount,
                          current_results_list)
        if close_parentheses < open_parentheses:
            build_balance(build_variant + ')',
                          open_parentheses,
                          close_parentheses + 1,
                          init_opened_amount,
                          current_results_list)
    return current_results_list


def BalancedParentheses(N):
    balanced_combinations = build_balance('', 0, 0, N, [])
    return ' '.join(balanced_combinations)

x = BalancedParentheses(4)
print(x)