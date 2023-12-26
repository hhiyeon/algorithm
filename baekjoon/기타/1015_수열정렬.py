n = int(input())
array = list(map(int, input().split()))
sorted_array = sorted(array)
answer = []

for idx in array:
    temp = sorted_array.index(idx)
    answer.append(temp)
    sorted_array[temp] = -1

print(*answer)
