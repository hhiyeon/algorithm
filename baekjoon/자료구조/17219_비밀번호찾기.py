from collections import defaultdict

n, m = map(int, input().split())  # 저장된 수, 찾으려는 수
site_info = defaultdict(str)

for _ in range(n):
    address, pwd = input().split(' ')  # 주소, 비밀번호
    site_info[address] = pwd

for _ in range(m):
    find_site = input()
    print(site_info[find_site])
