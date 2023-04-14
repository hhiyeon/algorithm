def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) # 문자열 리스트로 변환
    # numbers의 원소는 0~1000
    # x*3 : 3자리 수로 맞춰서 비교해준다.
    numbers.sort(key=lambda x: x*3, reverse = True)
    answer = str(int(''.join(numbers))) # '000' 인 경우 때문에 int -> str
    return answer