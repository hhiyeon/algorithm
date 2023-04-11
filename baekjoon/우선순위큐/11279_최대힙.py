import heapq
import sys

N = int(input())  # 연산의 개수
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if num > 0:  # 자연수인 경우 배열에 값 추가
        heapq.heappush(heap, -num)  # max heap은 지원하지 않아서, 데이터에 음수 값 붙이기
    elif num == 0:  # 0이면 배열에서 가장 큰 값 출력, 제거
        if len(heap) == 0:  # 배열이 비어있으면 0 출력
            print(0)
        else:
            print(-heapq.heappop(heap))
