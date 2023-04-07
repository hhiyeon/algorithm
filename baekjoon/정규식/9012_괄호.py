# 한 쌍의 괄호로 된 문자열 VPS
# 올바른 괄호 문자열이면 YES 아니면 NO

import re

tc = int(input())

for _ in range(tc):
    word = input()

    while True:
        temp = word.replace('()', '')
        if word == temp:
            if len(temp) == 0:
                print("YES")
            else:
                print("NO")
            break
        word = temp
