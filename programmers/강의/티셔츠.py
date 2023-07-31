def solution(people, tshirts):
    answer = 0
    people.sort()
    tshirts.sort()
    p, t = 0, 0
    while p < len(people) and t < len(tshirts):
        if tshirts[t] >= people[p]:
            answer += 1
            p += 1
        t += 1
    return answer
