def minimumAbsoluteDifference(arr):
    # Write your code here
    answer = float('inf')

    arr.sort()

    for i in range(1, len(arr)):
        a = arr[i-1]
        b = arr[i]
        answer = min(answer, abs(a-b), abs(b-a))

    print(answer)
    return answer


n = int(input())
array = list(map(int, input().split()))

minimumAbsoluteDifference(array)
