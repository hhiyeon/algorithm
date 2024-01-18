import sys

input = sys.stdin.readline
s, p = map(int, input().split())  # 문자열 길이, 부분문자열 길이
str_dna = (input())
acgt = list(map(int, input().split()))
answer = 0
check = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(p):
    check[str_dna[i]] += 1

if acgt[0] <= check['A'] and acgt[1] <= check['C'] and acgt[2] <= check['G'] and acgt[3] <= check['T']:
    answer += 1

for i in range(p, s):
    check[str_dna[i]] += 1
    check[str_dna[i - p]] -= 1
    if acgt[0] <= check['A'] and acgt[1] <= check['C'] and acgt[2] <= check['G'] and acgt[3] <= check['T']:
        answer += 1

print(answer)
