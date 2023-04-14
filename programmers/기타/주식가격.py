def solution(prices):
    answer = [0] * len(prices)

    for x in range(len(prices)):
        for y in range(x+1, len(prices)):
            if prices[x] <= prices[y]:
                answer[x] += 1
            else:
                answer[x] += 1
                break
    return answer
