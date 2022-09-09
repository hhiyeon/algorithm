def gcd(a,b):
    c=0
    while b!=0:
        c=a%b
        a=b
        b=c
    return a

def lcm(a,b):
    return (a*b) / gcd(a,b) 

def solution(arr):
    answer = 0
    
    while True:
        if len(arr)==1:
            answer = arr[0]
            break
        a = arr.pop()
        b = arr.pop()
        arr.append(lcm(a,b))
    return answer
