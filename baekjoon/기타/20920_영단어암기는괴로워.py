from collections import defaultdict
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
words = defaultdict(int)

for _ in range(n):
    w = input().strip()
    if len(w) >= m:
        words[w] += 1

sorted_words = sorted(words.items(), key=lambda x: [-x[1], -len(x[0]), x[0]])

for key, value in sorted_words:
    print(key)
