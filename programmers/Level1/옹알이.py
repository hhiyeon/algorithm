def cnt_result(babbling):
    default_words = ["aya", "ye", "woo", "ma"]
    cnt = 0

    for word in babbling:
        for x in default_words:
            if x * 2 in word:  # 중복 있으면 패스
                break
            word = word.replace(x, "9")

        if word.isdigit():
            cnt += 1

    return cnt


def solution():
    answer = cnt_result(["ayayeayayeayaaya", "ayaaya", "ayaye"])
    print(answer)


solution()
