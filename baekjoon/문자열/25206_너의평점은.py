total = 0
get_score = 0.0
score_array = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
               'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

for _ in range(20):
    title, score, opt = map(str, input().split())
    # print(title, score, opt)
    if opt != 'P':
        total += float(score)
        get_score += score_array[opt] * float(score)

print("{:0.6f}".format(get_score/total))
