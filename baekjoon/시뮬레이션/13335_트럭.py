n, w, L = map(int, input().split())  # 트럭의 수, 다리 길이, 다리 최대 하중

a_list = list(map(int, input().split()))  # n개의 정수 (트럭의 무게)
stack = [0] * w
second = 0

while stack:
    second += 1  # 1초 추가
    stack.pop(0)  # 첫 번째 요소 제거
    if a_list:  # 트럭이 남아 있는 경우
        element = a_list[0]
        if sum(stack) + element <= L:
            # 최대 하중을 넘지 않는 경우
            stack.append(element)
            del a_list[0]  # 첫 번째 요소 제거
        else:
            stack.append(0)

print(second)