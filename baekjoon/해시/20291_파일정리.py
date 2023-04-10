from collections import defaultdict

N = int(input())  # 파일의 개수
dict_file = defaultdict(int)

for _ in range(N):
    name, extension = input().split('.')  # 파일의 이름
    dict_file[extension] += 1

for key in sorted(dict_file):
    print('{0} {1}'.format(key, dict_file[key]))
