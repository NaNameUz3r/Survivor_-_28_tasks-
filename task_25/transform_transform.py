def TransformTransform(A, N):

    B = []

    for i in range(len(A) - 1):
        for j in range(len(A) - i - 1):
            k = i + j
            clown = max(A[j:k])
            B.append(clown)

    TransformTransform(B, N)

    return sum(B) % 2 == 0

