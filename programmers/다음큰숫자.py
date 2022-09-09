def solution(n):
    answer = 0
    element = n
    nCnt = bin(n)[2:].count('1')
    
    while True:
        element += 1
        binary = bin(element)[2:]
        oneCnt = binary.count('1')
        if nCnt == oneCnt:
            answer = int(binary, 2)
            break
    return answer
