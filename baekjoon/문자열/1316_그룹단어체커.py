from collections import defaultdict

n = int(input())
answer = 0

for _ in range(n):
    dict = defaultdict(int)
    word = input()
    before = word[0]
    dict[before] += 1
    flag = True
    for i in range(1, len(word)):
        cur = word[i]
        if before != cur and dict[cur] != 0:
            flag = False
            break
        dict[cur] += 1
        before = cur
    if flag:
        answer += 1
print(answer)
