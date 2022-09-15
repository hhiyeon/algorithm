# n = 2  # 로프의 개수
# arr = [10, 15]  # 로프가 버틸 수 있는 최대 중량
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr, reverse=True)
maxRes = 0 # 최대 무게

# 내림차순으로 들을 수 있는 로프 개수 * 현재 무게를 계산해서 최대값을 구해준다.
for k in range(n):
    maxRes = max(arr[k]*(k+1), maxRes)
print(maxRes)

