def calculate(remain, number):
    coin = remain // number
    remain = remain - (number * coin)
    return remain, coin


money = int(input())
remain = 1000 - money
answer = 0

for i in [500, 100, 50, 10, 5, 1]:
    res = calculate(remain, i)
    remain = res[0]
    answer += res[1]
    if remain == 0:
        break

print(answer)
