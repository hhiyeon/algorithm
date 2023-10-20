import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())  # 지원자 숫자
    scores = []
    for i in range(n):  # 서류 심사 성적, 면접 성적 순위
        doc, interview = map(int, input().split())
        scores.append([doc, interview])

    # 서류와 면접 중에 하나가 다른 지원자보다 떨어지지 않아야 선발
    # 선발할 수 있는 최대 인원 수 구하기
    sort_scores = sorted(scores)
    answer = 1
    min_value = sort_scores[0][1]

    for idx in range(1, len(sort_scores)):
        score = sort_scores[idx][1]
        if score < min_value:
            answer += 1
            min_value = min(min_value, score)

    print(answer)
