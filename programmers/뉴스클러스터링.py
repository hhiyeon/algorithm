from collections import Counter
def makeList(input):
    output = []
    for x in range(0, len(input)-1):
        if input[x].isalpha() and input[x+1].isalpha(): 
            tmp = input[x]+input[x+1]
            output.append(tmp)
    return output

def solution(str1, str2):
    answer = 0
    arr1 = makeList(str1.lower())
    arr2 = makeList(str2.lower())
            
    # 중복 개수
    cnt1 = Counter(arr1)
    cnt2 = Counter(arr2)
    
    intersection = list((cnt1&cnt2).elements())
    union = list((cnt1|cnt2).elements())
    
    if len(intersection)==0 and len(union) ==0:
        return 65536
    answer = int((len(intersection)/len(union))*65536)
    return answer
