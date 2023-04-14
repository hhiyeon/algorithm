queue1 = [1,2,1,2]
queue2 = [1,10,1,2]
from collections import deque
answer = 0
p1 = deque(queue1)
p2 = deque(queue2)
sum1 = sum(p1)
sum2 = sum(p2)

while True:
    if sum1 == sum2:
        break
    else:
        answer += 1
        if sum1 > sum2:
            e1 = p1.popleft()
            p2.append(e1)
            sum1 -= e1
            sum2 += e1
        else:
            e2 = p2.popleft()
            p1.append(e2)
            sum2 -= e2
            sum1 += e2
    if len(queue1)*3 < answer:
        answer = -1
        break
print(answer)
