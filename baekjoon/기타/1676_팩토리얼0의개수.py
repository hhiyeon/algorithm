def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


N = int(input())
answer = 0

for ch in str(factorial(N))[::-1]:
    if ch != '0':
        break
    answer += 1

print(answer)
