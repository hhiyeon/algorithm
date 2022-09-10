def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            # 같은 열 제외해서 큰 값 찾기
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[len(land)-1])
