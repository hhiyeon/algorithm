tc = int(input())

zero = [1,0,1]
one = [0,1,1]

def calculator(N):
    size = len(zero)
    if size <= N:
        for i in range(size, N+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[N], one[N])

for i in range(tc):
    N = int(input())
    calculator(N)
