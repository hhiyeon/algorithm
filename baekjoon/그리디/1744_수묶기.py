N = int(input())  # 수열의 크기
plus = []
minus = []
res = 0

for _ in range(N):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num == 1:
        res += 1
    else:
        minus.append(num)

plus.sort(reverse=True)
minus.sort()
plus_size, minus_size = len(plus), len(minus)

if len(plus) % 2 == 0:  # 양수 + 짝수 개수
    for idx in range(0, plus_size, 2):
        res += plus[idx] * plus[idx + 1]
else:  # 양수 + 홀수 개수
    res += plus[plus_size - 1]  # 마지막 값
    for idx in range(0, plus_size - 1, 2):
        res += plus[idx] * plus[idx + 1]

if len(minus) % 2 == 0:  # 음수 + 짝수 개수
    for idx in range(0, minus_size, 2):
        res += minus[idx] * minus[idx + 1]
else:  # 음수 + 홀수 개수
    res += minus[minus_size - 1]  # 마지막 값
    for idx in range(0, minus_size - 1, 2):
        res += minus[idx] * minus[idx + 1]

print(res)
