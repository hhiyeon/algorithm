def solution(cacheSize, cities): # 캐시크기, 도시이름 -> 총 실행시간 출력
    answer = 0
    # LRU : 가장 오랜 시간동안 사용하지 않은 페이지 교체 알고리즘
    # hit : 참조하려고 하는 메모리가 캐시에 있는 경우
    # miss : 참조하려는 메모리가 캐시에 없는 경우
    
    cache = []
    
    if cacheSize == 0:
        return len(cities)*5
    
    for x in range(len(cities)):
        current = cities[x].lower()
        if current in cache: # 캐시 안에 있는 경우
            # print(current, cache)
            answer += 1
            cache.remove(current)
            cache.append(current)
        else: # 캐시 안에 없는 경우
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(current)
            answer += 5
    return answer
