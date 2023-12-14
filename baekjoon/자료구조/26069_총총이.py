from collections import defaultdict
n = int(input())
dance = defaultdict(int)

for _ in range(n):
    a, b = map(str, input().split())

    if a == 'ChongChong' or b == 'ChongChong':
        dance[a] = 1
        dance[b] = 1

    elif dance[a] == 1 or dance[b] == 1:
        dance[a] = 1
        dance[b] = 1

print(sum(dance.values()))
