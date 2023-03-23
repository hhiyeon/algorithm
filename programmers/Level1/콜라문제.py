# 콜라 빈병 2개 -> 콜라 1병
# 보유 중인 빈병 2개 미만이면 콜라 X

# 필요한 병 개수, 마트가 주는 병 개수, 갖고 있는 빈병 개수
def bottle_result(a, b, n):
    count = 0
    extra_bottle = 0  # 여분의 병 개수 체크
    while n >= a or (extra_bottle + n) >= a:  # 빈병의 개수가 미달이 아닌 경우
        if extra_bottle != 0:
            n += extra_bottle
            extra_bottle = 0
        change_bottle = (n // a) * b
        if n / a != int(n / a): # 정수 체크 방법
            extra_bottle = n - (n//a * a)
        count += change_bottle
        n = change_bottle

    return count


def solution():
    answer = bottle_result(3,1,20)
    print(answer)


solution()
