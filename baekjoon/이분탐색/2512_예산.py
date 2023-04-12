N = int(input())  # 지방의 수
cost_list = list(map(int, input().split()))
M = int(input())  # 총 예산

# 총 예산 이하에서 가능한 최대 예산 구하기
cost_list.sort()
lt = 0
rt = cost_list[-1]
max_cost = float('-inf')

while lt <= rt:
    mid = (lt + rt) // 2
    total = 0
    for cost in cost_list:
        if cost > mid:
            total += mid
        else:
            total += cost

    if total <= M:  # 총 예산보다 적으면
        lt = mid + 1  # 상한가 증가
    else:
        rt = mid - 1  # 상한가 감소
print(rt)
