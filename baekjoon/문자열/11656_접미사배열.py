s = input()
stack = []
dictionary = []

for ch in s[::-1]:
    stack.append(ch)
    dictionary.append(''.join(stack[::-1]))

dictionary.sort()

for ch in dictionary:
    print(ch)
