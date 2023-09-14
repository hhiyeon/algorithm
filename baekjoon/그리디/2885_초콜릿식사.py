k = int(input())

# 가장 작은 초콜릿 크기, 최소 쪼갠 수
size = 1
cnt = 0

while size < k:
    size = size << 1  # 한 자리씩 2의 제곱 수

answer = size

while k > 0:
    if k >= size:  # 정사각형 초콜릿
        k -= size
    else:
        size //= 2
        cnt += 1  # 쪼갠 수

print(answer, cnt)