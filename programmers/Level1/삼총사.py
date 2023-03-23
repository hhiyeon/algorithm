# 3명의 번호가 0이 되면 삼총사
# 삼총사 개수 구하기
# 3명씩 조합을 만들어서 합을 구하고 합이 0인 개수 구하기
array = [-2, 3, 0, 2, -5]


def make_result():
    from itertools import combinations
    count = 0

    for x in combinations(array, 3):
        num_sum = sum(x)
        if num_sum == 0:
            count += 1
    print(count)
