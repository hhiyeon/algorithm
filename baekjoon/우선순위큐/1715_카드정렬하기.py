import heapq

N = int(input())  # 숫자 카드 묶음 개수
heap = []
total = 0

for _ in range(N):
    num = int(input())
    heapq.heappush(heap, num)
# A, B를 묶으려면 A+B 번의 비교

while heap:
    if len(heap) == 1:
        break
    if len(heap) > 1:
        min_value1 = heapq.heappop(heap)
        min_value2 = heapq.heappop(heap)
        add_value = min_value1 + min_value2
        total += add_value
        heapq.heappush(heap, add_value)

print(total)
