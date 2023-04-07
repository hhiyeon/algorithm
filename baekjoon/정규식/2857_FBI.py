import re

correct_cnt = 0
res_list = []

p = re.compile('FBI')

for idx in range(5):
    info = input()
    m = p.search(info)

    if m:
        correct_cnt += 1
        res_list.append(idx+1)

if correct_cnt == 0:
    print("HE GOT AWAY!")
else:
    print(' '.join(map(str, res_list)))