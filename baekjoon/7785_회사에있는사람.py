from collections import defaultdict
#n = 4 # 출입 기록 수
# arr = ['Baha enter', 'Askar enter', 'Baha leave', 'Artem enter']

# enter 출근, leave 퇴근
# 대소문자 구분
# 현재 회사에 있는 모든 사람을 구하는 프로그램 작성
n = int(input())
dict = defaultdict(str)

for x in range(n):
    name, opt = input().split()
    if dict[name] == 'enter' and opt == 'leave':
        del dict[name]
    else:
        dict[name] = opt

for x in sorted(dict.keys(),reverse=True):
    print(x)