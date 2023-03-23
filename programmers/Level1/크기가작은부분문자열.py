t = "3141592"
p = "271"
answer = 0
arr_size = len(p)

for i in range(len(t)-(arr_size-1)):
    sub_str = ''
    for j in range(arr_size):
        sub_str += t[i+j]
    if sub_str <= p:
        answer += 1

print(answer)
