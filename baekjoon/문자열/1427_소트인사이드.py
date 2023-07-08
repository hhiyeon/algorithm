n = int(input())
n_list = []

for i in str(n):
    n_list.append(int(i))

n_list.sort(reverse=True)

answer = ''

for i in n_list:
    answer += str(i)

print(int(answer))
