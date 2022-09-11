from collections import defaultdict
def solution(record):
    # 닉네임 변경 방법 - 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 모두 변경
    # 1. 채팅방을 나가고, 새로운 닉네임으로 들어온다.
    # 2. 채팅방에 입장한 상태에서, 닉네임을 변경한다.
    
    answer = []
    userDict = defaultdict(str)

    for x in range(len(record)):
        tmp = record[x].split(' ')
        opt = tmp[0]
        uid = tmp[1]
        if len(tmp) >2:
            nickname = tmp[2]
            userDict[uid] = nickname 
        if opt == 'Enter':
            answer.append(uid+'님이 들어왔습니다.')
        elif opt == 'Leave':
            answer.append(uid+'님이 나갔습니다.')
        elif opt == 'Change':
            # 이름 변경
            userDict[uid] = nickname
    
    for x in range(len(answer)):
        idx = answer[x].index('님')
        userList = answer[x][:idx]
        answer[x] = userDict[userList] + answer[x][idx:] 
    return answer
