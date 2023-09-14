S = input()
P = input()
answer = 1
idx = 0

for i in range(len(P)):
    if S.find(P[idx:i + 1]) >= 0:
        print(P[idx:i + 1], idx, i)
        continue
    idx = i
    answer += 1
print(answer)
