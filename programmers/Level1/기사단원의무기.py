# 기사단 번호 1~number
# 무기 구매 = 기사번호의 약수 개수
# 제한 수치보다 큰 공격력은 정해진 무기 구매
import math
def get_divisor(N):  # 약수 개수 구하는 함수
    count = 0
    for D in range(1, int(math.sqrt(N)) + 1):
        if N % D == 0:
            if D * D == N:
                count += 1
                break
            else:
                count += 2
    return count


def get_power_list(number, limit, power):
    divisor_list = []
    for i in range(1, number + 1):
        divisor_cnt = get_divisor(i)
        divisor_list.append(power if divisor_cnt > limit else divisor_cnt)
    return divisor_list


def solution():
    answer = sum(get_power_list(10, 3, 2))


solution()
