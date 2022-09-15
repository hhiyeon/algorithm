#n, s = 10, 15
#arr = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
n, s = map(int,input().split())
arr = list(map(int,input().split()))

lt = 0
rt = 0
minLen = float('inf')
value = 0

while True:
    # 수들의 합이 s를 넘으면 최소값을 계산
    # 안넘으면 rt 값 증가
    if value >= s:
        minLen = min(minLen, (rt - lt))
        value -= arr[lt]
        lt += 1
    elif rt == n:
        break
    else: # value < s:
        value += arr[rt]
        rt += 1

if minLen == float('inf'):
    minLen = 0

print(minLen)