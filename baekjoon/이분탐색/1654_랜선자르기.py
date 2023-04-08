# coding=utf-8
# k, n = 4, 11  # 이미 가지고 있는 랜선 개수, 필요한 랜선 개수 n
# kArr = [802, 743, 457, 539] # 랜선은 길이가 모두 다르다.
k, n = map(int, input().split())
kArr = []

for i in range(k):
    kArr.append(int(input()))
kArr = sorted(kArr) # 이분 탐색을 위한 정렬
lt = 0
rt = kArr[-1]
maxLen = 0

while lt <= rt:
    mid = (lt+rt)//2
    total = 0
    for size in kArr: # 구할 수 있는 랜선 개수 구하기
        total += (size//mid)

    if total >= n: # 랜선의 개수가 더 많을 경우
        maxLen = max(maxLen, mid) # 최대값 갱신
        lt = mid +1
    else:
        rt = mid -1 # 랜선의 개수가 부족할 경우 
print(maxLen)
