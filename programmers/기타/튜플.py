import re
def solution(s):
    answer = []
    arr = s.split(',{')
    arr.sort(key=len) # 길이 순으로 정렬
    
    for x in arr:
        # 숫자로 해당하는 항목들을 리스트로 변경
        numbers = re.findall('\d+', x)
        for k in numbers:
            if int(k) not in answer:
                answer.append(int(k))
    return answer
