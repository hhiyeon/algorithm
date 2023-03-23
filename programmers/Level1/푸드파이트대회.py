# A 선수 왼쪽부터 오른쪽으로
# B 선수 반대
# 중앙에 먼저 도달하는 선수가 승리
# food = [물, 1번음식개수, 2번음식개수, ...]
# 음식의 배치를 나타내는 문자열 Result 만들기

def food_location(food):
    # 왼쪽 문자열을 만들고 + 0 + 뒤집어서 오른쪽에 붙이기
    food_str = ''
    for index in range(1, len(food)):
        add_cnt = food[index] // 2
        food_str += add_cnt * str(index)
    reversed_str = food_str[::-1] # 문자열 거꾸로
    food_str = food_str + '0' + reversed_str
    return food_str


def solution():
    answer = food_location([1, 7, 1, 2])
    print(answer)


solution()
