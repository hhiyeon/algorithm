import sys

input = sys.stdin.readline
N = int(input())
lines = list(tuple(map(int, input().split())) for _ in range(N))
lines.sort()

left = lines[0][0]
right = lines[0][1]
total = 0

for idx in range(1, N):
    key, value = lines[idx]

    if key < right:
        right = max(value, right)
    else:
        total += right - left
        left, right = key, value

total += right - left
print(total)

# 1  2  3  4  5  6  7
# -------
#    ----------
#       -------
#                ----
#
# 4 + 1 = 5
