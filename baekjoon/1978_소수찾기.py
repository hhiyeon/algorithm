import math
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for x in arr:
    if isPrime(x):
        cnt += 1
print(cnt)
