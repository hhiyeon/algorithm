def solution(dirs):
    direction = {'U': (0, 1), 'L': (-1, 0), 'R': (1, 0), 'D': (0, -1)}
    x, y = (0, 0)
    visited = set()

    for d in dirs:
        nx, ny = x + direction[d][0], y + direction[d][1]

        if -5 <= nx <= 5 and -5 <= ny <= 5:  # 좌표 평면 끝
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            print(x, y, nx, ny)
            x, y = nx, ny

    return len(visited) // 2


print(solution("LULLLLLLU"))
