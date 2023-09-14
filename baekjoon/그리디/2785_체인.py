n = int(input())
chain_list = list(map(int, input().split()))

chain_list.sort()

# print(chain_list)
count = 1
idx = 0

while idx + count < len(chain_list):
    count += 1
    chain_list[idx] -= 1
    if chain_list[idx] == 0:
        idx += 1

print(count-1)