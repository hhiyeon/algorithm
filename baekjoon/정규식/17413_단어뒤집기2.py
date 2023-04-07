# 문자열 S에서 단어만 뒤집기

import re

S = input()
p = re.compile('<[a-z0-9 ]+>|[a-z0-9 ]')
m = p.findall(S)

result = ''
stack = ''
idx = 1

for word in m:
    if word[0] == '<':
        result += stack[::-1]
        result += word
        stack = ''
    else:
        if word == ' ':
            result += stack[::-1] + ' '
            stack = ''
        elif idx == len(m):
            stack += word
            result += stack[::-1]
            stack = ''
        else:
            stack += word
    idx += 1

print(result)
