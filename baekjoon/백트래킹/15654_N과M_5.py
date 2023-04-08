n, m = map(int, input().split())
# n, m = 4, 2 # n개의 수를 입력받고, m개의 중복없는 수열을 구하기
# arr = [9,8,7,1]
arr = list(map(int, input().split()))
arr = sorted(arr) # 사전순 출력
stack = []

def dfs():
    if len(stack) == m:
        for idx in stack:
            print(arr[idx], end=' ')
        print()
        return
    for x in range(0, n):
        if x not in stack:
            stack.append(x)
            dfs()
            stack.pop()
dfs()
