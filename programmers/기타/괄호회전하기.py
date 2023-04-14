def checkCondition(bracketStr):
    stack = []
    rightBracket = ['}', ')', ']']
    for x in range(len(bracketStr)):
        if len(stack) == 0:
            if bracketStr[x] in rightBracket:
                return False
            stack.append(bracketStr[x])
        else:
            if bracketStr[x] == '}' and stack[-1] == '{':
                stack.pop()
            elif bracketStr[x] == ')' and stack[-1] == '(':
                stack.pop()
            elif bracketStr[x] == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(bracketStr[x])
    if len(stack) == 0:
        return True
    return False
def solution(s):
    answer = 0
    
    for x in range(len(s)):
        if checkCondition(s): # 조건 만족시
            answer += 1
        # 괄호 회전
        s = s[1:] + s[0]
    return answer
