#n = 6
#arr = [10,20,10,30,20,50]
n = int(input())
arr = list(map(int, input().split()))
dp = [1]*n # 리스트로 반복되는 횟수를 저장한다.
for i in range(n):
	for j in range(i):
		if arr[i] > arr[j]:
			dp[i] = max(dp[i], dp[j]+1)

# print(dp)
# 1 2 1 3 2 4
# 10의 길이 1, 20의 길이 2, 10의 길이 ...
x = max(dp)
print(x)
res = []
for i in range(n-1, -1, -1):
	if dp[i] == x:
		res.append(arr[i])
		x -= 1

for i in res[::-1]:
	print(i, end=' ')
#print(res[::-1])