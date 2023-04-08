# 전파의 단위 0, 1

import re

tc = int(input())
p = re.compile('(100+1+|01)+')

for _ in range(tc):
    word = input()
    m = p.fullmatch(word)
    # match 와 다르게 fullmatch 는 처음 부터 끝까지 일치해야 한다.

    if m:
        print("YES")
    else:
        print("NO")