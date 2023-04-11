import heapq
import sys

T = int(input())  # 테스트 케이스

for _ in range(T):
    K = int(input())  # 소설 장 개수
    file_list = list(map(int, sys.stdin.readline().split()))  # 파일의 크기

    heapq.heapify(file_list)

    if K == 1:
        print(file_list[0])

    for x in file_list:
        heapq.heappush(file_list, x)

    total = 0

    while len(file_list) > 1:
        f1 = heapq.heappop(file_list)
        f2 = heapq.heappop(file_list)
        total += (f1 + f2)
        heapq.heappush(file_list, (f1 + f2))
    print(total)
