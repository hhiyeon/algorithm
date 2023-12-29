t = int(input())


def factorial(num):
    answer = 1
    for i in range(1, num + 1):
        answer *= i
    return answer


def get_combi_size(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


for _ in range(t):
    N, M = map(int, input().split())
    size = get_combi_size(M, N)
    print(size)
