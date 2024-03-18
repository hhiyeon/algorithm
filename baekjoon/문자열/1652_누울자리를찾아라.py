import re

n = int(input())
p = re.compile('[.]{2,}')
board = []
re_board = [[0] * n for _ in range(n)]
res1 = 0
res2 = 0

for _ in range(n):
    info = input()
    board.append(list(info))
    m = p.findall(info)
    res1 += len(m)

for i in range(n):
    for j in range(n):
        re_board[i][j] = board[j][i]

for i in range(n):
    m = p.findall(''.join(re_board[i]))
    res2 += len(m)

print(res1, res2)
