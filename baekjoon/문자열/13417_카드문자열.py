tc = int(input())

for _ in range(tc):
    n = int(input())  # 카드 개수
    card_alpha = list(input().split())  # 카드에 적힌 알파벳 초기 순서
    answer = card_alpha[0]

    for i in range(1, n):
        alpha = card_alpha[i]
        if ord(answer[0]) >= ord(alpha):
            answer = alpha + answer
        else:
            answer += alpha
    print(answer)

