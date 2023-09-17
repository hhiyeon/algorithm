address = input()  # IPv6 주소

array = address.split(':')
result = []
# print(array)
flag = False

for i in range(len(array)):
    if array[i] == '':
        if len(array) >= 8 and flag:
            continue
        result.append('0000:')
        if not flag and len(array) < 8:
            for _ in range(8-len(array)):
                result.append('0000:')
        flag = True
    else:
        result.append(array[i].zfill(4) + ':')

print(''.join(result)[:-1])
