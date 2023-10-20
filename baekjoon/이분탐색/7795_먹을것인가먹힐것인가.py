tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())  # a의 수, b의 수
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    a_list.sort()
    b_list.sort()
    #print(a_list, b_list)

    answer = 0
    b_idx = 0

    for x in a_list:
        while b_idx < m and x > b_list[b_idx]:
            b_idx += 1
        answer += b_idx
    print(answer)
