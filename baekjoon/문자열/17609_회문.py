# 회문 0, 유사회문 1, 그 이외 2 출력

T = int(input())  # 문자열의 개수


def second_check(word, lt, rt):
    while lt < rt:
        if word[lt] == word[rt]:
            lt += 1
            rt -= 1
        else:
            return False
    return True


for _ in range(T):
    s = input()
    lt = cnt = 0
    rt = len(s) - 1

    if s == s[::-1]:
        print("0")
        continue

    while lt < rt:
        if s[lt] == s[rt]:  # 같을 경우 왼쪽 증가, 오른쪽 감소
            lt += 1
            rt -= 1
        else:  # 다른 부분이 나오면 유사 회문인지 아예 아닌지 확인하기
            # 왼쪽, 오른쪽 둘중에 어느 부분 삭제하는지 확인
            word_lt = second_check(s, lt + 1, rt)
            word_rt = second_check(s, lt, rt - 1)
            if word_rt or word_lt:
                print("1")
                break
            else:
                print("2")
                break
