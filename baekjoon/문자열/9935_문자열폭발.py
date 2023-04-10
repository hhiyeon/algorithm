S = input()  # 문자열
P = input()  # 폭발 문자열

stack = []

for ch in S:
    stack.append(ch)
    if ch == stack[-1] and ''.join(stack[-len(P):]) == P:
        del stack[-len(P):]

res = ''.join(stack)

if len(res) == 0:
    print("FRULA")
else:
    print(res)