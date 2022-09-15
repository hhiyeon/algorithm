# n, k = 10, 4200  # 동전 종류, 구하려는 값 - 동전의 최소 개수 구하기
# arr = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr, reverse=True)
cnt = res = 0

for x in arr:
    if k >= x:
        cnt = k // x
        res += cnt
        k = k - (x * cnt)
    if k <= 0:
        break
print(res)