def transform(numbers_to_transform):

    back_keys = []
    coef = 0
    for outer_index in range(0, len(numbers_to_transform)):
        for inner_index in range(0, len(numbers_to_transform) - outer_index):
            coef = outer_index + inner_index
            major_number = 0
            for find_max in range(inner_index, coef + 1):
                if major_number <= numbers_to_transform[find_max]:
                    major_number = numbers_to_transform[find_max]
            back_keys.append(major_number)
    return back_keys


def TransformTransform(A, N):

    key = transform(transform(A))
    return sum(key) % 2 == 0

