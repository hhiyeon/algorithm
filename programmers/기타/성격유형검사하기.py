from collections import defaultdict


def solution(survey, choices):
    # 두 성격 유형 중 사전 순으로 빠른 성격 유형 검사자 유형
    # 검사자 유형 결과 지표 번호 순서 대로 출력
    answer = ''
    dict_type = defaultdict(int)
    n = len(survey)

    for idx in range(n):
        user_type = ''
        opt = choices[idx]

        if opt < 4:  # 왼쪽 타입 1~3점
            score = 4 - opt
            user_type = survey[idx][0]
        elif opt > 4:  # 오른쪽 타입
            score = opt - 4
            user_type = survey[idx][1]
        else:  # 4점은 패스
            continue

        dict_type[user_type] += score

    def get_type(a_type, b_type):
        if dict_type[a_type] < dict_type[b_type]:
            return b_type
        else:
            return a_type

    answer += get_type('R', 'T')
    answer += get_type('C', 'F')
    answer += get_type('J', 'M')
    answer += get_type('A', 'N')

    return answer


# RT CF JM AN
s = ["AN", "NA", "RT", 'TR']
c = [4, 3, 2, 1]
print(solution(s, c))
