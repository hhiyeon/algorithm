s = input()
stack = []
check = ['P', 'P', 'A', 'P']

for i in range(len(s)):
    stack.append(s[i])
    if stack[-4:] == check:
        for _ in range(4):
            stack.pop()
        stack.append('P')
    # print(stack)

if stack == ['P']:
    print("PPAP")
else:
    print("NP")