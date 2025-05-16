"""
1. 조건
- K개의 각자 다른 랜선을 활용하여 동일한 길이의 N개의 랜선을 만들어야 함.
- 자르고 남은 것은 버러야 함

2. N개 만들 수 있는 최대 랜선의 길이

3. 시간 제한
- x < O(N^2)
"""

import sys 
input = sys.stdin.readline

def solution(M, cables):
    # start = 0 // ZeroDivisionError 발생
    start = 1
    end = max(cables)
    result = 0
    
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        
        for cable in cables:
            cnt += (cable//mid)
        
        
        if cnt >= M:
            start = mid + 1
            result = mid 
        else:
            end = mid -1
    
    return result
        

if __name__ == '__main__':
    K, M = map(int, input().split())
    
    cables = list()
    for i in range(K):
        cables.append(int(input()))

    print(solution(M, cables))
        