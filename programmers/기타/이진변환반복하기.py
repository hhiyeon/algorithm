def solution(s):
    answer = [0,0]
    zero = 0
    
    while True:
        if s == '1':
            break
        zero = s.count('0') # 제거할 0의 개수
        s = s.replace('0', '')
        s = bin(len(s))[2:] # 이진 변환 결과
        answer[0] += 1
        answer[1] += zero
    return answer
