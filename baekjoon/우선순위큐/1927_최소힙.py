import heapq
import sys

N = int(input())  # 연산의 개수
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if num > 0:  # 자연수인 경우 : 배열에 값 추가
        heapq.heappush(heap, num)
    elif num == 0:  # 0 : 배열에서 가장 작은 값 출력 + 제거
        if len(heap) == 0:  # 배열이 비어 있는 경우 0 출력
            print(0)
        else:
            print(heapq.heappop(heap))
