def transform(numbers_to_transform):

    B = []

    for i in range(0, len(numbers_to_transform) - 1):
        for j in range(0, len(numbers_to_transform) - i - 1):
            k = i + j
            try:
                clown = max(numbers_to_transform[j:k])
                B.append(clown)
            except ValueError:
                continue

    return B


def TransformTransform(A, N):

    key = transform(transform(A))
    return sum(key) % 2 == 0

