#최대 경로 합
def dogfood(matrix):
    if not matrix:
        return 0
    rows, cols = (len(matrix), len(matrix[0]))
    dp = [[0] * cols for _ in range(rows)]

    #1행 복사
    for j in range(cols):
        dp[0][j] = matrix[0][j]

    #최대 경로 합 계산
    for i in range(1, rows):
        for j in range(cols):
            dp[i][j] = matrix[i][j] + max(dp[i - 1][j], dp[i][max(0, j - 1)])
    return dp


#행렬 입력
def get():
    m = []
    row, col = map(int, input().split())
    for _ in range(row):
        m.append(list(map(int, input().split())))
    return m


#좌표 계산
def findfood(Sum, rr, cc):
    cnt = []
    j, k = rr - 1, cc - 1

    while j > 0 or k > 0:
        cnt.append((j, k))
        if j == 0:
            k -= 1
        elif k == 0:
            j -= 1
        else:
            if Sum[j - 1][k] > Sum[j][k - 1]:
                j -= 1
            else:
                k -= 1

    cnt.append((0, 0))

    return cnt[::-1]


#행렬 입력
matrix = get()

#경로 합
result = dogfood(matrix)

#좌표
path = findfood(result, len(matrix), len(matrix[0]))

for coord in path:
    print(coord[::-1])
