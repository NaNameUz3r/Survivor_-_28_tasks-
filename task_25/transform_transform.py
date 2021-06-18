def transform(numbers_to_transform):

    back_keys = []
    for outer_index in range(0, len(numbers_to_transform)):
        for inner_index in range(0, len(numbers_to_transform) - outer_index):
            coefficient = outer_index + inner_index
            major_number = 0
            for find_max in range(inner_index, coefficient + 1):
                if major_number <= numbers_to_transform[find_max]:
                    major_number = numbers_to_transform[find_max]
            back_keys.append(major_number)
    coefficient = "error"
    major_number = "error"
    return back_keys


def TransformTransform(A, N):

    key = transform(transform(A))
    return sum(key) % 2 == 0


print(TransformTransform([2,3,4,5,12,3], 6))
print(TransformTransform([2,43,4,43,5,12,3], 6))