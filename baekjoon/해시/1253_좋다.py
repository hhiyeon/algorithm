from itertools import combinations

N = int(input())  # 수의 개수
num_list = list(map(int, input().split()))
combi = combinations(num_list, 2)
answer = set()

for item in list(combi):
    total = sum(item)
    if total in num_list:
        answer.add(total)

print(len(answer))
