import re

word = input()
check = input()

p = re.compile(check)
m = p.findall(word)

print(len(m))