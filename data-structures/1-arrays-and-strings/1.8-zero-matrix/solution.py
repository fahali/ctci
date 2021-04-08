def zero_matrix(mx):
    rows = []
    cols = []

    for row in range(len(mx)):
        for col in range(len(mx[row])):
            if mx[row][col] == 0:
                rows.append(row)
                cols.append(col)

    for row in rows:
        for col in range(len(mx[row])):
            mx[row][col] = 0

    for col in cols:
        for row in range(len(mx)):
            mx[row][col] = 0

    return mx


m = [
    [1, 1, 1, 1, 1],  # [1, 0, 1, 1, 0]
    [1, 1, 1, 1, 0],  # [0, 0, 0, 0, 0]
    [1, 0, 1, 1, 1],  # [0, 0, 0, 0, 0]
    [1, 1, 1, 1, 0],  # [0, 0, 0, 0, 0]
    [1, 1, 1, 1, 1],  # [1, 0, 1, 1, 0]
]

print(zero_matrix(m))
