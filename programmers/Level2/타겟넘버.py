def solution(numbers, target):
    answer = 0

    def dfs(idx, cost):
        if idx >= len(numbers):  # 인덱스가 크면 종료
            if cost == target:  # 구하는 값일때 cnt
                nonlocal answer
                answer += 1
            return
        dfs(idx + 1, cost + numbers[idx])  # 현재 원소를 포함
        dfs(idx + 1, cost - numbers[idx])  # 현재 원소를 포함 X

    dfs(0, 0)
    return answer


solution([1, 1, 1, 1, 1], 3)

n, s = map(int, input().split())  # 정수의 개수, 정수 S
numbers = list(map(int, input().split()))
