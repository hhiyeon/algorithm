n = int(input())
board = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

answer = 0
for a in board:
    answer += sum(a)

print(answer)
