# 수열 A가 주어질 때, 가장 긴 증가하는 부분 수열 구하기
n = 6
arr = [10, 20, 10, 30, 20, 50]
lis = [0]

for case in arr:
    if lis[-1] < case:
        lis.append(case)
    else:
        left = 0
        right = len(lis)

        while left < right:
            # print(lis)
            mid = (left+right)//2
            if lis[mid] < case:
                left = mid + 1
            else:
                right = mid
        lis[right] = case
print(lis[1:])