# 최소 강의실 개수 구하기
import heapq
import sys

input = sys.stdin.readline
N = int(input())  # 수업의 개수

class_list = []

for _ in range(N):
    x, y = map(int, input().split())
    class_list.append([x, y])

class_list.sort()
heap = []
heapq.heappush(heap, class_list[0][1])  # 첫 번째 강의 끝나는 시간
# heap 최소 힙 유지 = 0 번째 인덱스는 가장 작은 값

for idx in range(1, N):
    start, end = class_list[idx]
    if start < heap[0]: # 빠른 시작 시간 < 앞에서 가장 빨리 끝나는 값
        heapq.heappush(heap, end) # 새 강의실 추가
    else: # 강의실 유지, 강의 시간 갱신
        heapq.heappop(heap)
        heapq.heappush(heap, end)
print(len(heap))
