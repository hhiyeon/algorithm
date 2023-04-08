# 동전 종류 N개, 합을 K로 만드려고 할 때 최소 동전 개수

N, K = map(int, input().split())
money_list = []

for _ in range(N):
    money_list.append(int(input()))

sorted_money = sorted(money_list, reverse=True)

coin_cnt = 0

for money in sorted_money:
    if K < money:
        continue
    else:
        coin_num = K // money
        # print(K, money, coin_num)
        K = K - (money * coin_num)
        coin_cnt += coin_num
    if K == 0:
        break

print(coin_cnt)
