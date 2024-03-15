alpha = input()
n = int(input())
answer = 0

for _ in range(n):
    ring = input()

    for idx in range(len(ring)):
        find = ring[idx:idx + len(alpha)]
        count = len(alpha) - len(find)
        find = find + ring[:count]
        if alpha == find:
            answer += 1
            break
print(answer)
