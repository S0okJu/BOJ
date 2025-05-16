from collections import deque
from typing import List

import sys 
input = sys.stdin.readline

LION = 1
APEACH = 2

def solution(K:int, dolls:List[int]) -> int:
    result = float('inf')
    work_q = deque([])
    for idx, doll in enumerate(dolls):
        if doll == LION:
            work_q.append(idx)
        
        if len(work_q) == K:
            result = min(work_q[-1] - work_q[0] + 1, result)
            work_q.popleft()
    
    return -1 if result == float('inf') else result

if __name__ == '__main__':
    N, K = map(int,input().split())
    dolls = list(map(int,input().split()))
    print(solution(K, dolls))