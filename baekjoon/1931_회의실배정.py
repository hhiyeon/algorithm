n = int(input())  # 회의 수 - 회의가 겹치지 않게 진행할 수 있는 회의 최대 개수 구하기
arr = [[0] * 2 for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    arr[i][0] = a # 회의 시작 시간
    arr[i][1] = b # 회의 끝나는 시간

#n = 11
#arr = [[1, 1], [1, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
n = 3
arr = [[1,1],[1,1],[0,1]]
arr.sort(key=lambda x: (x[1], x[0])) # 두번째 값이 같은 경우, 첫번째 값으로 오름차순
time = cnt = start = end = 0

for element in arr:
    start = element[0]
    end = element[1]
    if time <= start:
        time = end
        cnt += 1
print(cnt)