from collections import deque
import sys
n = int(input())
queue = deque()

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'pop_front': # 덱의 가장 앞의 수를 빼고 출력, 덱에 정수 없으면 -1 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif command[0] == 'pop_back': # 덱의 가장 뒤의 수를 빼고 출력, 덱에 정수 없으면 -1 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
            queue.pop()
    elif command[0] == 'size': # 덱의 정수 개수 출력
        print(len(queue))
    elif command[0] == 'empty': # 덱이 비어있으면 1 아니면 0 출력
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front': # 덱의 가장 앞의 수 출력, 없으면 -1 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back': # 덱의 가장 뒤의 수 출력, 없으면 -1 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif command[0] == 'push_front': # 정수 x를 덱의 앞에 넣는다.
        queue.appendleft(command[1])

    elif command[0] == 'push_back': # 정수 x를 덱의 뒤에 넣는다.
        queue.append(command[1])