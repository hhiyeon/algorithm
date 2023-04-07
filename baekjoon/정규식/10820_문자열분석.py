# 문자열 N개
# 소문자, 대문자, 숫자, 공백의 개수 구하기

import sys
import re

p1 = re.compile('[a-z]')
p2 = re.compile('[A-Z]')
p3 = re.compile('[0-9]')
p4 = re.compile(' ')

while True:
    word = sys.stdin.readline().rstrip('\n')

    if not word:
        break

    m1 = p1.findall(word)
    m2 = p2.findall(word)
    m3 = p3.findall(word)
    m4 = p4.findall(word)

    print(len(m1), len(m2), len(m3), len(m4))
