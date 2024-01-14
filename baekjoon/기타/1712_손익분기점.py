a, b, c = map(int, input().split())
# 고정비용, 가변비용, 총수입
answer = 0

if c - b <= 0:
    print(-1)
else:
    # 총 수입
    total = a / (c - b)
    print(int(total) + 1)
