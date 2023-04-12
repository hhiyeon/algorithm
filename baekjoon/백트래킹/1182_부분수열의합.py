n, s = map(int, input().split())  # 정수의 개수, 정수 S
numbers = list(map(int, input().split()))

# n, s = 5, 0
# numbers = [-7, -3, -2, 5, 8]
cnt = 0


# 크기가 양수인 부분 수열 중에서 다 더한 값이 S인 경우의 수 구하기

def dfs(idx, cost):
    global cnt
    if idx >= n:  # 인덱스가 정수 개수보다 크면 종료
        return
    cost += numbers[idx]  # 더한값 += 현재 값
    if cost == s:  # 더한 값이 s면 경우의수 + 1
        cnt += 1
    dfs(idx + 1, cost)  # 현재 원소를 포함하는 경우
    dfs(idx + 1, cost - numbers[idx])  # 현재 원소를 포함하지 않는 경우


dfs(0, 0)
print(cnt)
