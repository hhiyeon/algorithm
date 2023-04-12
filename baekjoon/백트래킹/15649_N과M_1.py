n, m = 4, 4
# n, m = map(int, input().split())
s = []


def dfs():
    if len(s) == m:  # 리스트의 길이가 m개인 경우
        print(' '.join(map(str, s)))  # 리스트의 모든 숫자들을 출력
        return
    for i in range(1, n + 1):  # 1부터 n+1
        if i not in s:  # 리스트 안에 i(1~4) 가 없으면
            s.append(i)  # 리스트에 i(1~4) 추가
            dfs()  # 다음 레벨
            s.pop()  # 마지막으로 넣었던 i 제거


dfs()
