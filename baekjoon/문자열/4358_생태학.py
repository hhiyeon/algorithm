import sys
from collections import defaultdict
input = sys.stdin.readline

dict_trees = defaultdict(int)
total = 0

while True:
    tree = input().rstrip()
    if tree == '':
        break

    dict_trees[tree] += 1
    total += 1

for key in sorted(dict_trees):
    value = dict_trees[key]
    percent = (value/total * 100)
    print('{0} {1:0.4f}'.format(key, percent))

