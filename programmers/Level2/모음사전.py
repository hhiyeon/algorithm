from itertools import product


def solution(word):
    answer = 0
    dictionary = []

    for i in range(1, 6):
        for x in product(["A", "E", "I", "O", "U"], repeat=i):  # 모음, 중복가능한 수
            dictionary.append(''.join(list(x)))  # 조합을 문자열로 만들어서 사전에 넣기

    dictionary.sort()  # 조합들을 정렬
    return dictionary.index(word) + 1