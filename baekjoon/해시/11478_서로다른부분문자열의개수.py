S = input()
set_list = set()
n = len(S)

for i in range(n):
    for j in range(i, n):
        element = S[i:j + 1]
        set_list.add(element)

print(len(set_list))
