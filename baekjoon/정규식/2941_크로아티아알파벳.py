import re

word = input()
p = re.compile('c=|c-|dz=|d-|lj|nj|s=|z=|[a-z]')
m = p.findall(word)

print(len(m))