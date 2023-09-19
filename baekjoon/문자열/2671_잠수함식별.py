import re

s = input()
pattern = '(100+1+|01)+'  # (100~1~|01)~

# match : 시작부터 패턴과 일치하는 첫 번째 문자열 찾기
# search : 패턴과 일치하는 첫 번째 문자열 찾기

m = re.fullmatch(pattern, s)

if m:
    print("SUBMARINE")
else:
    print("NOISE")
