from collections import defaultdict
import math
def solution(fees, records): 
    # 주차요금 - 기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)  
    # 자동차입/출차내역 - 시간(시:분), 차량번호, 내역(입차or출차)
    # 차량 번호가 작은 자동차부터 청구 금액 출력
    answer = []
    timeDict = defaultdict(str)
    totalDict = defaultdict(int)
    
    # 차량 번호마다, 총 사용 시간을 구한다. - 출차내역이 없으면 23:59 출차
    for x in range(len(records)):
        tmp = records[x].split(' ')
        hour = tmp[0]
        carNum = tmp[1]
        opt = tmp[2]
        
        if opt == 'IN':
            timeDict[carNum] = hour
        else:
            resTime = 0
            inTime = timeDict[carNum]
            inHour = int(inTime[:2])
            inMinute = int(inTime[-2:])
            outHour = int(hour[:2])
            outMinute = int(hour[-2:])
            timeDict[carNum] = '' # 초기화
            
            # 출차 시간(분) 계산
            if outMinute < inMinute:
                resTime = (outHour - inHour - 1)*60
                resTime += (60 - inMinute) + outMinute
            else:
                resTime = (outHour - inHour)*60
                resTime += (outMinute - inMinute)
            # 차량 번호의 사용 시간 업데이트
            totalDict[carNum] = totalDict.get(carNum, 0) + resTime 

    # 출차 기록이 없는 차량 번호 23:59으로 계산
    for key, value in timeDict.items():
        if len(value) != 0:
            time = (59 - int(value[-2:])) + (23 - int(value[:2]))*60
            totalDict[key] = totalDict.get(key, 0) + time

    # 요금 계산
    for key, value in totalDict.items():
        if value <= fees[0]: # 시간이 넘지 않은 경우
            totalDict[key] = fees[1] # 기본 요금
        else:
            remain = fees[1] + math.ceil((value - fees[0]) / fees[2]) * fees[3]
            totalDict[key] = remain

    # 차량번호별 정렬
    sorted_dict = dict(sorted(totalDict.items()))

    for i in sorted_dict.values():
        answer.append(i)
    return answer
