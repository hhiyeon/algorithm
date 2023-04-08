# n = 5  # 정수의 개수
# arrA = [1, 1, 1, 6, 0]  # A 정수 배열
# arrB = [2, 7, 8, 3, 1]  # B 정수 배열

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_A = sorted(A)
sorted_B = sorted(B, reverse=True)

# print(sorted_A, sorted_B)

total = 0
for idx in range(N):
    total += sorted_A[idx] * sorted_B[idx]

print(total)
