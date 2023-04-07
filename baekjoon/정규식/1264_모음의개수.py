# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성
# 모음 a e i o u, 대문자 또는 소문자

import re
p = re.compile('[aeiouAEIOU]')

while True:
    sentence = input()
    if sentence == '#':
        break

    m = p.findall(sentence)
    print(len(m))
