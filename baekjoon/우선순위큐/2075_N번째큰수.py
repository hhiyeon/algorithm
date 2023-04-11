import heapq

N = int(input())  # N 번째로 큰 수 찾기
heap = []
num_list = []

for _ in range(N):
    num_list = list(map(int, input().split()))

    for x in num_list:
        if len(heap) < N:  # 메모리 N 까지 제한
            heapq.heappush(heap, x)
        else:
            if heap[0] < x:  # 힙의 최소 값보다 입력 값이 더 큰 경우
                heapq.heappop(heap)
                heapq.heappush(heap, x)

print(heapq.heappop(heap))
