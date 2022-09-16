import heapq
n = int(input()) # 숫자 카드 묶음 개수
heap = []
answer = 0

for _ in range(n):
    x = int(input())
    heapq.heappush(heap, x)

while len(heap)!=1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    answer += a + b
    heapq.heappush(heap, a+b)

print(answer)