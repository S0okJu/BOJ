from typing import List, Tuple

import sys 
input = sys.stdin.readline

def solution(C:int, investments:List[Tuple[int,int]]) -> int:
    customers = [float("inf")] * (C+101)
    customers[0] = 0
    
    for money, potential in investments:
        for idx in range(1, C+101):
            customers[idx] = min(customers[idx], customers[idx-potential] + money)
    
    return min(customers[C:])
        
if __name__ == '__main__':
    C, N = map(int,input().split())
    
    investments = list()
    for i in range(N):
        a, b = map(int,input().split())
        investments.append((a,b))
    
    print(solution(C,investments))