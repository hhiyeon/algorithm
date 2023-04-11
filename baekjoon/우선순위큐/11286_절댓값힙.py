import heapq
import sys

n = int(input())  # 연산의 개수 18
# arr = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0]  # 연산에 대한 정보
# 0 x : 배열에서 절댓값이 가장 작은 값 출력하고 값 제거
# 1 x : 값을 넣는 연산
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:  # 값 넣기
        heapq.heappush(heap, (abs(x), x))  # 절댓값 abs(값), 기존 값
    else:
        # 배열에서 절댓값이 가장 작은 값 출력하고 값 제거
        # 같은 값이 여러개면 가장 작은 수 출력
        # 배열이 비어있으면 0 출력
        if len(heap) == 0:
            print(0)
        else:  # 튜플은 (a,b) 형태일 때 a부터 비교 후에 b를 비교
            element = heapq.heappop(heap)
            print(element[1])
