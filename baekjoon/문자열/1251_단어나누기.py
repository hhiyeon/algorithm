word = input()
answer = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]

        answer.append(''.join(a[::-1] + b[::-1] + c[::-1]))

print(min(answer))