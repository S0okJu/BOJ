from heapq import heappush, heappop
from collections import deque
from typing import List
import sys 
input = sys.stdin.readline

def timeout(N:int, jewels:List, K:int, bags:List ) -> int:
    q = []
    # 보석 Max Heap으로 정렬 
    for i in range(N):
        heappush(q,(-jewels[i][1],jewels[i][0]))
    
    # 가방 올림차순 정렬 
    bags.sort()
    is_contain = [False for _ in range(K)]
    price = 0 
    while q and bags:
        vc, mc = heappop(q)
        # print(vc)
        for k in range(K):
            if is_contain[k]:
                continue
            # 가방의 최대 무게보다 모석의 무게가 더 작다면 
            if mc <=bags[k]:
                if not is_contain[k]:
                    # 값을 더한다. 
                    price += (vc) * -1
                    is_contain[k] = True
                    break
                
    return price            

def solution(N:int, jewels:List, K:int, bags:List ) -> int:
    
    # 보석 Max Heap으로 정렬 
    jewels_q = deque(sorted(jewels))
    q = []
    
    # 가방 올림차순 정렬 
    bags.sort()
    price = 0 

    for bag in bags:
        while jewels_q and jewels_q[0][0] <= bag:
            # 담을 수 있는 모든 보석을 담는다. 
            m,v = jewels_q.popleft()
            
            # 가격을 담는다. 
            heappush(q, -v)
        
        # 가능한 보석이 있으면 하나 뽑아서 가방에 답는다. 
        if q:
            price -= heappop(q)
    return price  

if __name__ == '__main__':
    
    N, K = map(int, input().split())
    jewels = []
    for i in range(N):
        mi, vi = map(int,input().split())    
        jewels.append((mi,vi))
    
    bags = []
    for j in range(K):
        bags.append(int(input()))
    
    print(solution(N,jewels, K,bags))
    
    
