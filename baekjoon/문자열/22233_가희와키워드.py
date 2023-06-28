from collections import defaultdict
import sys

n, m = map(int, sys.stdin.readline().split())
dict = defaultdict(int)

for i in range(n):
    keyword = sys.stdin.readline().rstrip()
    dict[keyword] = 1
cnt = n
for j in range(m):
    keyword = sys.stdin.readline().rstrip().split(',')
    for k in keyword:
        if dict[k] == 1:
            dict[k] = 0
            cnt -= 1

    print(cnt)
