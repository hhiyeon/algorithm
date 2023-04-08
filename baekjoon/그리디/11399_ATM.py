# N 명의 사람 (1~N번)
# Pi = i번째 사람 인출 소요 시간

N = int(input())
cost = list(map(int, input().split()))
cost_list = []

for idx in range(N):
    cost_list.append((idx, cost[idx]))

sorted_list = sorted(cost_list, key=lambda x: x[1])
res = total_sum = 0

for key, value in sorted_list:
    total_sum += value
    res += total_sum

print(res)
