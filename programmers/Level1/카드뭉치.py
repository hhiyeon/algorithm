# 10:48
from collections import deque


def check_goal(cards1, cards2, goal):
    dq1 = deque(cards1)
    dq2 = deque(cards2)

    for word in goal:
        flag = False
        if len(dq1) != 0 and dq1[0] == word:
            dq1.popleft()
            flag = True
            continue
        if len(dq2) != 0 and dq2[0] == word:
            dq2.popleft()
            flag = True
            continue
        if not flag:
            return "No"  # 둘다 해당 X
    return "Yes"


def solution():
    answer = check_goal(["i", "water", "drink"],
                        ["want", "to"],
                        ["i", "want", "to", "drink", "water"])
    print(answer)


solution()
