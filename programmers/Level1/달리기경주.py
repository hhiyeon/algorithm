def solution(players, callings):
    dict = {}

    for i in range(len(players)):
        name = players[i]
        rank = i + 1
        dict[name] = rank

    for p1 in callings:
        dict[p1] -= 1
        p2 = players[dict[p1] - 1]
        dict[p2] += 1
        n1, n2 = dict[p1] - 1, dict[p2] - 1
        players[n1], players[n2] = players[n2], players[n1]

    return players