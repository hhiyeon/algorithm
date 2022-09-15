# n = 5  # 정수의 개수
# arrA = [1, 1, 1, 6, 0]  # A 정수 배열
# arrB = [2, 7, 8, 3, 1]  # B 정수 배열

n = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort(reverse=True)
res = 0

for x in range(n):
    res += arrA[x]*arrB[x]

print(res)
