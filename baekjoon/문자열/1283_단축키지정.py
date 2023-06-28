import sys

n = int(sys.stdin.readline())  # 옵션 개수
keyword = []
answer = []

for _ in range(n):
    opt = sys.stdin.readline().split()
    flag = True

    for idx in range(len(opt)):
        if opt[idx][0].upper() not in keyword:
            keyword.append(opt[idx][0].upper())
            opt[idx] = "[" + opt[idx][0] + "]" + opt[idx][1:]
            flag = False
            print(' '.join(opt))
            break

    if flag:  # 문자 첫 글자가 변경이 안됬으면
        # 알파벳 앞에부터
        for i in range(len(opt)):
            for j in range(len(opt[i])):
                if opt[i][j].upper() not in keyword:
                    keyword.append(opt[i][j].upper())
                    opt[i] = opt[i][:j] + '[' + opt[i][j] + ']' + opt[i][j + 1:]
                    flag = False
                    print(' '.join(opt))
                    break
            if not flag:
                break

    if flag:
        print(*opt)