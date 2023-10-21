def find_maximum_path_sum(matrix):
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])

    # 자료구조, 0으로 초기화 [[0,..0], [0,..0], [0,..0]]
    dp = [[0] * cols for _ in range(rows)]

    # 맨 윗줄의 값은 그냥 복사
    for j in range(cols):
        dp[0][j] = matrix[0][j]

    # 위에서 2번째줄부터 아래로 내려가면서 최대 합 계산
    for i in range(1, rows):
        for j in range(cols):
            dp[i][j] = matrix[i][j] + max(dp[i-1][j], dp[i-1][max(0, j-1)], dp[i-1][min(cols-1, j+1)])

    max_sum = max(dp[rows-1])
    return max_sum

matrix = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
]
result = find_maximum_path_sum(matrix)
print(f"가장 높은 합: {result}")