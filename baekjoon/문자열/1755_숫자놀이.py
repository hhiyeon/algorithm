m, n = map(int, input().split())
arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
       'seven', 'eight', 'nine', 'ten']
dictionary = {}
answer = []

for idx in range(len(arr)):
    dictionary[arr[idx]] = str(idx)

for idx in range(m, n + 1):
    temp = ''
    for num in str(idx):
        temp += str(arr[int(num)])
    answer.append(temp)

answer.sort()
count = 1

for name in answer:
    for key, value in dictionary.items():
        if key in name:
            name = name.replace(key, value)
    print(name, end=' ')
    if count % 10 == 0:
        print()
    count += 1
