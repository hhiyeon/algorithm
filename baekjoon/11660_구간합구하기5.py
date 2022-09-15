import sys
# n, m = 4, 3 # 표의 크기, 연산 횟수
n, m = map(int, input().split())
arr = [[0]*(n+1)] + list([0]+list(map(int, input().split())) for _ in range(n))
sumArr = [[0]*(n+1) for _ in range(n+1)]

# 누적합 배열 만들기
for i in range(1, n+1):
    for j in range(1, n+1):
        sumArr[i][j] = sumArr[i-1][j] + sumArr[i][j-1] - sumArr[i-1][j-1] + arr[i][j]

# 계산 하기 - (x1, y1) 부터 (x2, y2) 합 구하기
# 전체 - 영역1 - 영역2 + (영역1과 영역2에서 두번 빼줬기 때문에 더해줘야 하는 영역)
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    res = sumArr[x2][y2] - sumArr[x1-1][y2] - sumArr[x2][y1-1] + sumArr[x1-1][y1-1]
    print(res)
