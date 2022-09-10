import math
def isPrime(num):
    if num == 1:
        return False
    for x in range(2, int(math.sqrt(num) + 1)):
        if num % x == 0:
            return False
    return True
def solution(n, k):
    answer = 0
    tmp = ''
    
    # k진법 계산
    while n!=0:
        tmp += str(n%k)
        n //=k
    tmp = tmp[::-1] # 거꾸로 뒤집기
    
    arr = tmp.split('0')
    
    for x in range(len(arr)):
        if len(arr[x]) != 0 and isPrime(int(arr[x])): 
            answer += 1
    return answer
