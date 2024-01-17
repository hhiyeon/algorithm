m = int(input())
array = []

for _ in range(m):
    word = input()
    temp = ''
    idx = 0

    for ch in word:
        if idx == 0:
            if ch.isdigit() and ch != '0':
                temp += ch
        else:
            if ch.isdigit():
                temp += ch
            else:
                # print('알파벳', temp)
                if len(temp) != 0:
                    array.append(int(temp))
                    temp = ''
        idx += 1
    if len(temp) != 0:
        array.append(int(temp))

array.sort()

for num in array:
    print(num)
