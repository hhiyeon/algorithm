while True:
    try:
        n, m, b = map(float, input().split(' '))
        # 저금액, 이자율, 구하는 금액
        year = 0
        while True:
            if b <= n:
                break
            n = n + (n * (m / 100))
            year += 1
        print(year)
    except:
        break
