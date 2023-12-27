n, kim, lim = map(int, input().split())
answer = 0

while kim != lim:
    kim -= kim//2
    lim -= lim//2
    answer += 1

print(answer)
