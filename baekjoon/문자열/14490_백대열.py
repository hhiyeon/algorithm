n, m = map(int, input().split(':'))


def gcd(a, b):
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b


value = gcd(n, m)
print(str(n // value)+':'+str(m // value))
