# 트럭 한 대로 배송할 수 있는 최대 박스 수 출력
N, C = map(int, input().split())  # 마을의 수, 트럭 용량
M = int(input())  # 박스 정보 개수
info = []
res = 0

for _ in range(M):
    # 박스를 보내는 마을, 박스를 받는 마을, 보내는 박스의 개수
    from_box, to_box, num_box = map(int, input().split())
    info.append((from_box, to_box, num_box))

sort_info = sorted(info, key=lambda x: x[1]) # 가장 빨리 받는 순서대로 정렬
remain = [0] * (N+1) # 남은 상자

for item in sort_info:
    start, end, box = item[0], item[1], item[2]
    max_box = box
    for i in range(start, end): # 시작점부터 도착지까지 보낼 수 있는 박스 개수
        max_box = min(max_box, C - remain[i])
    # print(max_box, C-remain[i])
    for j in range(start, end):
        remain[j] += max_box
    res += max_box
print(res)


