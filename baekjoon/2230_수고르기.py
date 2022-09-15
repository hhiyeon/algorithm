n, m = 5, 3  # 정수 개수, 두 개의 정수 차이 최소 기준
arr = [1, 2, 3, 4, 5]
#n, m = map(int, input().split())
#arr = [int(input()) for _ in range(n)]
arr.sort()
lt = 0
rt = 0
minValue = float('inf')
# print(arr)
while rt != n and lt <= rt:
    value = arr[rt] - arr[lt]
    if value >= m:  # m 이상일 때
        minValue = min(minValue, value)
        lt += 1
    else:  # m 이상이 아닐 때
        rt += 1
print(minValue)
