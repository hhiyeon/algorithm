# 입력된 문자열 확인
# 문자열의 길이는 7
# 문자열의 문자는 2종류
# AABBABB 형식 만족

import re

tc = int(input())

for _ in range(tc):
    command = input()

    if len(command) != 7:
        print(0)
        continue

    set_command = set(list(command))

    if len(set_command) != 2:
        print(0)
        continue

    # AABBABB 형식 만족
    first = command[0]
    diff = ''

    for x in command:
        if first != x:
            diff += x
            break

    pattern = first * 2 + diff * 2 + first + diff * 2
    p = re.compile(pattern)
    m = p.search(command)

    if m:
        print(1)
    else:
        print(0)

    # if command[0] == command[1] == command[4] and command[2] == command[3] == command[5] == command[6]:
    #     print(1)
    # else:
    #     print(0)
