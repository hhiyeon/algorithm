def solution(phone_book):
    answer = True
    dict = {}

    for x in phone_book:
        dict[x] = 1

    for str in phone_book:
        tmp = ''
        for idx in str:  # 각 문자를 넣어주고
            tmp += idx  # 딕셔너리에 존재하고, 비교하는 문자열과 같지 않은 경우
            if tmp in dict and tmp != str:
                return False
    return answer