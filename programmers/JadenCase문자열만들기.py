def solution(s):
    answer = ''
    s = s.split(' ')

    for x, y in enumerate(s):
        if y == '':
            continue
        if not s[x][0].isdigit():
            s[x] = y.title()
        else:
            s[x] = y[0] + y[1:].lower()
    answer = ' '.join(s)

    return answer