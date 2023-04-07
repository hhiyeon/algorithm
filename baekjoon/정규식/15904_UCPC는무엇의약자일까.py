# 대소문자 구분
# UCPC으로 만들 수 있으면 I love UCPC 출력, 안되면 I hate UCPC


import re

word = input()
p = re.compile('.*U.*C.*P.*C.*')
m = p.match(word)

if m:
    print("I love UCPC")
else:
    print("I hate UCPC")

# ACUCPCA