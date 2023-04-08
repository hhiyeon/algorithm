N = int(input())
score = []
res = 0

for _ in range(N):
    score.append(int(input()))

for idx in range(N - 1, 0, -1):
    if score[idx] <= score[idx - 1]:
        del_score = score[idx - 1] - score[idx] + 1
        res += del_score
        score[idx - 1] = score[idx] - 1

print(res)
