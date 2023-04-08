import sys
from collections import deque

n = int(input())
dq = deque(enumerate(map(int, input().split())))
answer = []

while dq:
    idx, nextIdx = dq.popleft()
    answer.append(idx+1)

    if nextIdx > 0:
        dq.rotate(-(nextIdx-1))
    else:
        dq.rotate(-nextIdx)

print(*answer)

