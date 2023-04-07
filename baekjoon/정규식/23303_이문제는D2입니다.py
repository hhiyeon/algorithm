# 문자열 안에 D2나 d2가 있으면 D2출력

import re
p = re.compile('D2|d2')
word = input()
m = p.search(word)

if m:
    print('D2')
else:
    print('unrated')