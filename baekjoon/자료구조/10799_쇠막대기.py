words = input()
answer = 0
stack = []

# print(words)

for i in range(len(words)):
    if words[i] == '(':
        stack.append(words[i])
    else:
        if words[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
    # print(answer, w, stack)

print(answer)