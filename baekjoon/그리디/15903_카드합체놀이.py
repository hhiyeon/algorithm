# 최소 점수 구하기
n, m = map(int, input().split())  # 카드의 개수, 합체 횟수
a_list = list(map(int, input().split()))  # 카드 상태

for _ in range(m):
    a_list = sorted(a_list)
    a_list[0] = a_list[1] = a_list[0] + a_list[1]

print(sum(a_list))
