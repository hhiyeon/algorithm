#n, m = map(int, input().split())
s = [] 

def dfs(start):
    if len(s) == m: # 리스트의 길이가 m개인 경우
        print(' '.join(map(str, s))) # 리스트의 모든 숫자들을 출력
        return 
    for i in range(start, n+1): # start으로 1,1 2,2, 3,3
        s.append(i) # 리스트에 i(1~4) 추가
        dfs(i) # 다음 레벨
        s.pop() # 마지막으로 넣었던 i 제거
dfs(1)
