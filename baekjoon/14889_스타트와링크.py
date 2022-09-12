n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
minValue = float('inf')
t1 = [] # 스타트팀
# t2 = [] # 링크팀

# 스타트팀 - 링크팀 능력치 최소값 출력
# (1,3,6) (2,4,5) -> 13,31,16,61,36,63
def calculator(combList):
    total = 0
    for x in range(len(combList)):
        a = combList[x][0]-1
        b = combList[x][1]-1
        total += (arr[a][b] + arr[b][a])
    return total

def dfs(start):
    global minValue
    if len(t1) == n//2:
        t2 = []
        diff = 0
        for i in range(1, n+1):
            if i not in t1:
                t2.append(i)
        combList1 = list(comb(t1, 2))
        combList2 = list(comb(t2, 2))
        total1 = calculator(combList1)
        total2 = calculator(combList2)
        diff = abs(total1 - total2)

        if minValue > diff:
            minValue = diff
    else:
        for idx in range(start, n+1):
            if idx not in t1:
                t1.append(idx)
                dfs(idx)
                t1.pop()
dfs(1)
print(minValue)
