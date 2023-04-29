def divStr(p): # 문자열 u,v 분리
    leftCnt = 0
    rightCnt = 0
    
    for x in range(len(p)):
        if p[x]=='(':
            leftCnt += 1
        if p[x]==')':
            rightCnt += 1

        if leftCnt == rightCnt:
            return p[:x+1], p[x+1:] # u, v
    
def checkStr(u): # 올바른 괄호 문자열인지 체크
    stack = []
    for x in u:
        if x == '(':
            stack.append(x)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    answer = ''
    
    # 1번 - 빈 문자열이면 빈 문자열 반환
    if not p:
        return ""
        
    # 2번 - u, v으로 분리
    u, v = divStr(p)
    
    # 3번 - u가 올바른 문자열이면 v에 대해 1단계부터 수행
    # 수행한 결과 문자열을 u에 이어 붙이고 반환한다.
    if checkStr(u):
        return u + solution(v)
    else:
        # 4번 - u가 올바르지 않은 문자열인 경우
        # 4-1번 빈 문자열에 첫 번째 문자로 '(' 붙이기
        answer = '('
        
        # 4-2번 문자열 v에 대해 1단계부터 재귀적으로 수행하고 결과를 이어 붙이기
        answer += solution(v)
        
        # 4-3번 ')' 붙이기
        answer += ')'
        
        # 4-4번 u의 첫 번째 마지막 문자 제거, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙이기
        for x in u[1:len(u)-1]:
            if x == '(':
                answer += ')'
            else:
                answer += '('
        
    return answer
