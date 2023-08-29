def solution(keymap, targets):
    answer = []

    for word in targets:
        total = 0

        for ch in word:
            sum = float('inf')
            flag = False
            for key in keymap:
                if ch in key:
                    sum = min(key.index(ch)+1, sum)
                    flag = True
            if not flag:
                total = -1
                break
            total += sum
        answer.append(total)
    print(answer)
    return answer




solution(["ABACD", "BCEFD"], ["ABCD", "AABB"])
print()
solution(["AGZ", "BSSS"], ["ASA", "BGZ"])