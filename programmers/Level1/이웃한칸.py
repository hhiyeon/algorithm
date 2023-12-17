def solution(board, h, w):
    answer = 0
    n = len(board)
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]

    for d in range(4):
        nx = h + x[d]
        ny = w + y[d]

        if 0 <= nx < n and 0 <= ny < n and board[h][w] == board[nx][ny]:
            answer += 1
    return answer
