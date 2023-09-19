tc = int(input())

for _ in range(tc):
    n = int(input())
    answer = 0


    # ASCII 순서에 따라 결과가 0이 되는 모든 수식 출력

    def cal(total, sign, i, num, arr):
        if i == n:
            total = total + (sign*num)
            if total == 0:
                print(arr)
        else:
            # print(total, i, num, arr)
            right = i + 1
            cal(total, sign, right, num * 10 + right, arr + ' ' + str(right))
            cal(total + sign * num, 1, right, right, arr + '+' + str(right))
            cal(total + sign * num, -1, right, right, arr + '-' + str(right))


    cal(0, 1, 1, 1, '1')
    print()
