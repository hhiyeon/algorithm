import base64

S = input()

# base64로 변환하려면
# 문자열을 byte으로 타입 변환 해야 한다.
s_byte = S.encode('ascii')
print(s_byte)

# byte 타입을 base64로 변환한다.
s_base64 = base64.b64encode(s_byte)
print(s_base64)

# base64 타입을 byte 타입으로 디코딩
res_s = s_base64.decode('ascii')
print(res_s)