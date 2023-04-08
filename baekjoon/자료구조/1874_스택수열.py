#n = 8 # 정수의 개수, 최대 정수값
#arr = [4,3,6,8,7,5,2,1]
n = int(input())
stack = []
maxIdx = 1
answer = []
flag = False

# push 오름차순
for i in range(n):
    x = int(input())
    while maxIdx <= x:
        stack.append(maxIdx)
        answer.append('+')
        maxIdx += 1

    if stack[-1] == x:
        stack.pop()
        answer.append('-')

    else: #stack[-1] != x:
        flag = True
        break


if flag:
    print('NO')
else:
    for x in answer:
        print(x)