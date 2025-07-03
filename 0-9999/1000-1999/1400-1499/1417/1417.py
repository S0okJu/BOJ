from typing import List
from heapq import heappush, heappop, heapify
import sys 
input = sys.stdin.readline

def solution(N:int, cands:List[int])->int:
    if N == 1:
        return 0
    
    dasom = cands[0]
    heap = [-1 * cand for cand in cands[1:]]
    heapify(heap)
    
    result= 0
    while -heap[0] >= dasom:
        curr = -heappop(heap)
        result += 1
        curr -=1
        dasom +=1
        
        heappush(heap,-curr)
    
    return result
    
if __name__ == '__main__':
    N = int(input())
    cands = [int(input()) for _ in range(N)]
    
    print(solution(N=N, cands=cands))
    