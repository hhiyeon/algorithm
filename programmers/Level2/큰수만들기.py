def get_result(number, k):
    num_list = []
    for item in number:
        while num_list and k > 0 and num_list[-1] < item:
            num_list.pop()
            k -= 1
        num_list.append(item)

    return ''.join(num_list[:len(number) - k])


def solution(number, k):
    answer = get_result(number, k)
    print(answer)
    return answer


solution("1231234", 3)
