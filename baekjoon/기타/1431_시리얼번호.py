n = int(input())
array = []

for _ in range(n):
    array.append(input())


def get_sum(number):
    res = 0
    for num in number:
        if num.isdigit():
            res += int(num)
    return res


sorted_array = sorted(array, key=lambda x: [len(x), get_sum(x), x])

for i in sorted_array:
    print(i)
