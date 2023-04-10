S = list(map(str, input()))  # S 문자열을
T = list(map(str, input()))  # T 문자열로 바꾸는 게임

# 문자열의 뒤에 A 추가 -> 뒤의 A 제거
# 문자열을 뒤집고 뒤에 B 추가 -> 뒤의 B 제거, 뒤집기

while len(S) != len(T):
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)
