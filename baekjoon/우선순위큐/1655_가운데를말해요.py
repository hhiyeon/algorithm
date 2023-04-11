import heapq
import sys

N = int(input())

lt_heap = []  # 최대힙
rt_heap = []  # 최소힙
for _ in range(N):
    num = int(sys.stdin.readline())

    # 중간값 = N 개의 수 중에서 중간에 위치한 값
    # 왼쪽힙, 오른쪽힙에 값을 번갈아 넣어준다.
    if len(lt_heap) == len(rt_heap):
        heapq.heappush(lt_heap, -num)
    else:
        heapq.heappush(rt_heap, num)

    # lt 에서 rt로 최소값 넣기
    if rt_heap and rt_heap[0] < -lt_heap[0]:
        lt_value = heapq.heappop(lt_heap)
        rt_value = heapq.heappop(rt_heap)
        heapq.heappush(lt_heap, -rt_value)
        heapq.heappush(rt_heap, -lt_value)

    print(-lt_heap[0])
