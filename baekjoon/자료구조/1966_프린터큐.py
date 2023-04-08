from collections import deque

tc = int(input()) # 테스트 케이스 수
for _ in range(tc):
    n, m = map(int, input().split()) # 문서 개수, 찾을 위치
    arr = list(map(int, input().split())) # 문서 중요도 배열
    pq = deque() # 덱으로 큐 생성

    # (인덱스, 중요도) 값으로 덱 요소 삽입
    for x in range(len(arr)):
        pq.append((x, arr[x]))
    importList = sorted(arr, reverse=True)  # 중요도 순서
    importIdx = 0
    cnt = 0
    while pq:
        element = pq.popleft()
        if importList[importIdx] == element[1]:  # 중요도 순서가 맞는 경우
            importIdx += 1
            cnt += 1
            if element[0] == m:  # 찾는 인덱스와 일치할 경우
                print(cnt)
                break
        else:
            pq.append(element)  # 맨 왼쪽 오른쪽에 삽입