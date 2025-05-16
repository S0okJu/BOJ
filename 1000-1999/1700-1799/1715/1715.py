from heapq import heappush, heappop,heapify
from typing import List 

import sys 
input = sys.stdin.readline

def solution(N:int, cards:List[int]) -> int:
    heapify(cards)
    sum_ = 0
                    
    while len(cards) > 1:
        first = heappop(cards)
        second = heappop(cards)
        
        cost = first + second 
        sum_ += cost 
        
        heappush(cards, cost)
            
    return sum_
        
if __name__ =='__main__':
    N = int(input())
    
    cards = []
    for i in range(N):
        cards.append(int(input()))
    
    print(solution(N=N, cards=cards))
