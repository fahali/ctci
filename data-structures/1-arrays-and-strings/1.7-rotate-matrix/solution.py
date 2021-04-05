def rotate_matrix(mx):
    N = len(mx)
    # assuming mx is N x N big
    grid = [[None for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            grid[i][j] = mx[N - j - 1][i]

    return grid


m = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]

print(rotate_matrix(m))  # [['G', 'D', 'A'], ['H', 'E', 'B'], ['I', 'F', 'C']]
