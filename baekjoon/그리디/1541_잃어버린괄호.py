num = input().split('-')
total = 0

for plus in num[0].split('+'):
    total += int(plus)

for minus in num[1:]:
    sub_sum = sum(map(int, minus.split('+')))
    total -= int(sub_sum)
print(total)
