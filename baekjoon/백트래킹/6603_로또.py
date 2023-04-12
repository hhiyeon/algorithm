def dfs(stack, numbers, start, k):
    if len(stack) == 6:
        print(' '.join(map(str, stack)))
        return
    for x in range(start, len(numbers)):
        dfs(stack + [numbers[x]], numbers, x + 1, k)


while True:
    num = list(map(int, input().split()))
    if num[0] == 0:
        break

    k = num[0]  # 번호 개수
    numbers = sorted(num[1:])  # 번호 리스트

    visited = [False] * len(numbers)
    dfs([], numbers, 0, k)
    print()
