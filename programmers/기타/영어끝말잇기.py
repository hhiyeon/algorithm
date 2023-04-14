def solution(n, words):
    answer = [0, 0]
    pArr = [0] * (n+1)
    stack = []
    prev = ''

    for x in range(len(words)):
        pNum = x+1
        if pNum > n:
            pNum %=3
            pNum = pNum % n
            if pNum == 0:
                pNum = n

        if words[x] not in stack:
            stack.append(words[x])
            pArr[pNum] += 1
            if len(prev) > 0 and prev[-1] != words[x][0]:
                answer[0] = pNum
                answer[1] = pArr[pNum]
                break
        else:
            answer[0] = pNum
            answer[1] = pArr[pNum] + 1
            break
        prev = words[x]
    return answer
