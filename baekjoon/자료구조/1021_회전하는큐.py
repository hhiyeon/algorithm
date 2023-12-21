from collections import deque

n, m = map(int, input().split())  # 큐 크기, 뽑는 개수
check = list(map(int, input().split()))  # 수 위치 순서대로
arr = deque([i + 1 for i in range(n)])
answer = 0

for num in check:
    while True:
        if arr[0] == num:
            arr.popleft()
            break
        else:
            if arr.index(num) <= len(arr) // 2:
                arr.rotate(-1)
                answer += 1
            else:
                arr.rotate(1)
                answer += 1

print(answer)
