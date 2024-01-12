k = int(input())

for idx in range(k):
    diff = []
    array = list(map(int, input().split()))
    sorted_array = sorted(array[1:])

    for i in range(len(sorted_array) - 1):
        diff.append(sorted_array[i + 1] - sorted_array[i])

    print('Class', idx + 1)
    print('Max {0}, Min {1}, Largest gap {2}'.format(max(array[1:]), min(array[1:]), max(diff)))
