import sys

n, c = map(int, sys.stdin.readline().split())  # 집의 개수, 공유기 개수
x_arr = []

for _ in range(n):
    x = int(sys.stdin.readline())  # 집의 좌표
    x_arr.append(x)

x_arr.sort()

res = 0
start = 1  # 최소 거리 1
end = x_arr[-1] - x_arr[0]  # 최대 거리 = 가장 먼거리

while start <= end:
    mid = (start + end) // 2  # 중간값 = 현재 가능한 공유기 사이의 거리
    temp = x_arr[0]  # 이전 집의 좌표
    cnt = 1

    for i in range(1, n):
        if x_arr[i] - temp >= mid:  # 가능한 거리(mid) 이상으로 공유기를 설치할 수 있는 집에 공유기 설치
            cnt += 1
            temp = x_arr[i]

    if cnt >= c:  # c개 이상의 공유기를 설치할 수 있는지 확인
        start = mid + 1  # 가능하면 mid 증가
        res = mid
    else:
        end = mid - 1  # 불가능하면 mid 감소

print(res)
