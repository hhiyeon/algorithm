#M = 26 # 연산의 수
import sys
M = int(sys.stdin.readline())
S = 0 # 공집합

for _ in range(M):
    command = sys.stdin.readline().split()
    opt = command[0]
    if len(command)>1:
        x = int(command[1]) - 1

    if opt == 'add': # S에 x를 추가한다.
        S = S | (1 << x)
    elif opt == 'remove': # S에서 x를 제거한다.
        S = S & ~(1 << x)
    elif opt == 'check': # S에 x가 있으면 1을, 없으면 0 출력
        if S & (1 << x) == 0:
            print(0)
        else:
            print(1)
    elif opt == 'toggle': # S에 x가 있으면 x 제거, 없으면 x 추가
        S = S ^ (1 << x)
    elif opt == 'all': # S를 {1,2, ..., 20} 으로 바꾼다.
        S = (1 << 20)-1
    elif opt == 'empty': # S를 공집합으로 바꾼다
        S = 0
