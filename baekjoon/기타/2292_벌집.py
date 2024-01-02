n = int(input())
answer = 1

for idx in range(n):
    answer += idx * 6
    if n <= answer:
        print(idx+1)
        break
