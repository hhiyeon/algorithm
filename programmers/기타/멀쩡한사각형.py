def gcd(a, b):
    c = 0
    while b!=0:
        c = a%b
        a = b
        b = c
    return a
def solution(w,h):
    answer = 1
    answer = (w*h) - (w+h-gcd(w,h))
    return answer
