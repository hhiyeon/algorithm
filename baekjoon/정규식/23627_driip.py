# driip 으로 끝나는 문자 찾기

import re
p = re.compile('driip$')
word = input()

m = p.search(word)

if m:
    print('cute')
else:
    print('not cute')
