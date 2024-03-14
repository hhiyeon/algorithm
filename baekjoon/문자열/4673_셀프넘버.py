n = 1
answer = set()

while n < 10000:
    total = n
    arr = []
    for i in range(len(str(n))):
        total += int(str(n)[i])
        arr.append(int(str(n)[i]))
    n = n + 1
    answer.add(total)

for i in range(1, 10000):
    if i not in answer:
        print(i)
