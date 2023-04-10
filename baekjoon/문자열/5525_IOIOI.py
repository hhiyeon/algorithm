N = int(input())  # Pn, 정수
M = int(input())  # S의 길이
S = input()  # 문자열

answer = idx = cnt = 0

while idx < (M - 1):
    if S[idx: idx + 3] == "IOI":
        idx += 2
        cnt += 1
        if cnt == N:
            answer += 1
            cnt -= 1
    else:
        idx += 1
        cnt = 0

print(answer)
