n = 3
op = [3,4,5] # 주어진 수열 - 순서 바꾸기 X
add, sub, mul, div = 1, 0, 1, 0  # 덧셈 뺄셈 곱셈 나눗셈 개수
#n = int(input())
#op = list(map(int, input().split()))
#add, sub, mul, div = map(int, input().split())
minValue = float('inf')
maxValue = float('-inf')

def dfs(i, arr):
    global minValue, maxValue, add, sub, mul, div
    if i == n:
        # 최대값 최소값 구하기
        maxValue = max(maxValue, arr)
        minValue = min(minValue, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, arr+op[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr-op[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, arr*op[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(arr/op[i]))
            div += 1

dfs(1, op[0])
print(maxValue)
print(minValue)
