S = input()

for idx in range(len(S)):
    if S[idx:] == S[idx:][::-1]:
        # idx 에서 시작한 문자열과 그 문자열을 거꾸로 뒤집은 문자열 확인
        print(len(S) + idx)  # 같은 문자열을 찾으면, 그 문자열 길이 + 추가해야 하는 문자 개수
        break
