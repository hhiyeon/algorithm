from itertools import combinations
from itertools import permutations
import heapq
from itertools import product
from collections import deque
from collections import defaultdict
from collections import Counter

queue = deque()
dict1 = {}
dict2 = defaultdict(int)
board = [[0 for _ in range(5)] for _ in range(5)]
heap = []
array = [2, 3, 4, 5, 1, 2]
counter = Counter(array)
# print(counter.most_common(1), counter[2])

ex1 = 'hello'
ex2 = '123'
ex3 = ' 공백제거 '
print(ex1.isdigit(), ex2.isdigit())
print(ex1.isalpha(), ex2.isupper(), ex1.islower())
print(ex3.strip(), ex1[::-1])
print(bin(2)[2:].zfill(4), oct(2), hex(2), ord('a'), chr(97))
print(''.join(map(str, array)))
temp = ex1.replace('h', 'w')
print(temp)

print(counter.items())