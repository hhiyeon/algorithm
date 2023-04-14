from itertools import combinations
from collections import Counter

def solution(orders, course): 
    # 코스요리 재구성 - 최소 2가지 이상 단품메뉴 + 최소 2명 이상이 시킨 메뉴, 인기 메뉴 
    answer = []
    for k in course:
        tmp = []
        for menu in orders:
            menuList = combinations(sorted(menu), k) # k개씩 오름차순 조합 만들기
            tmp += menuList
        cnt = Counter(tmp) # 만들어진 조합 리스트들 중에서, 각 원소들의 중복 수를 구해준다.
        
        # cnt.values() 조합의 개수를 출력 조합이 없고, 중복 개수가 1인 경우 출력 X
        if len(cnt) != 0 and max(cnt.values()) != 1:
            for x in cnt:
                if cnt[x] == max(cnt.values()):
                    answer.append(''.join(x))
    answer.sort()
    return answer
