#n, m = 5, 11 # 문자열 개수
# n개의 줄에 집합 S에 포함되어 있는 문자열
# m개의 줄에 검사하는 문자열이 주어진다.
# m개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력

from collections import defaultdict
n, m = map(int, input().split())
answer = 0
S = defaultdict(int)
for x in range(n):
    key = input()
    S[key] = 1

for x in range(m):
    key = input()
    if S[key]:
        answer += 1
print(answer)