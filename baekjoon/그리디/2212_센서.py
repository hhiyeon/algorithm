n = int(input())
k = int(input())
array = list(map(int, input().split()))
array.sort()

answer = []
for i in range(0, n - 1):
    answer.append(array[i + 1] - array[i])

answer.sort()
print(sum(answer[:n-k]))
