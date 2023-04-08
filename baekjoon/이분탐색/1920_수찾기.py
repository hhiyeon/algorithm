# n = 5
# a = [4, 1, 5, 2, 3]
# m = 5
# b = [1, 3, 7, 9, 5]
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a = sorted(a)
maxVal = a[-1]

for element in b:
    lt = 0
    rt = n - 1
    res = 0

    if maxVal >= element:
        while lt <= rt:
            mid = (lt + rt) // 2
            print(element, lt, rt, mid, a[mid], res)
            if a[mid] == element:
                res = 1
                break
            elif a[mid] < element:
                lt = mid +1
            else:
                rt = mid -1
    print(res)