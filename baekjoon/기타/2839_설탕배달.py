n = int(input())
res = 0

while n > 0:
    if n % 5 == 0:
        res += (n // 5)
        n -= (n//5 * 5)
        break
    res += 1
    n -= 3

if n != 0:
    print(-1)
else:
    print(res)

