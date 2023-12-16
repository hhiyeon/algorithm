def solution(bandage, health, attacks):
    answer = health
    cnt = 0  # 시간
    idx = 0
    skill = 0

    while cnt < attacks[-1][0]:
        cnt += 1
        skill += 1
        if cnt == attacks[idx][0]:
            answer -= attacks[idx][1]
            if answer <= 0:
                return -1
            idx += 1
            skill = 0
        else:
            answer = min(health, answer + bandage[1])
            if skill == bandage[0]:
                answer = min(health, answer + bandage[2])
                skill = 0

    return answer


# 기술 시간, 회복량, 추가 회복량 / 최대 체력 / 몬스터 공격 시간, 피해량
print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
