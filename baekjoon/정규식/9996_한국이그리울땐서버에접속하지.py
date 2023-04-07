import re

tc = int(input())
pattern = list(map(str, input().split('*')))
str_pattern = '^' + pattern[0] + '.*' + pattern[1] + '$'
#p = re.compile("^{0}[a-z]*{1}$".format(pattern[0], pattern[1]))
p = re.compile(str_pattern)

for _ in range(tc):
    word = input()
    m = p.search(word)
    if m:
        print("DA")
    else:
        print("NE")

# 2
# ab*bd
# abbd
# ab
