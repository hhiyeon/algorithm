import math
import sys
#m, n = 3, 16 # m 이상 n 이하 소수 모두 출력
m, n = map(int, sys.stdin.readline().split())

def isPrime(num):
    if num == 1:
        return False
    for x in range(2, int(math.sqrt(num) + 1)):
        if num % x == 0:
            return False
    return True

for i in range(m, n+1):
    if isPrime(i):
        print(i)