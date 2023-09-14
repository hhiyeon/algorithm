n = int(input())
s = list(map(int, input().split()))
total = []

s.sort()
# print(s)

for i in range(len(s) // 2):
    total.append(s[i] + s[len(s) - i - 1])

print(min(total))