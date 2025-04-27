from typing import List 

import sys 
input = sys.stdin.readline

def solution(N:int, M:int, A:List[int])->int:
    start, end = 0, 0
    
    count = 0
    sum_ = 0
    while start < N:
        if sum_ < M and end < N:
            sum_ += A[end]
            end +=1
        else:
            sum_ -= A[start]
            start +=1
        
        if sum_ == M:
            count += 1
    return count 
            
    
if __name__ == '__main__':
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
     
    print(solution(N=N,M=M,A=A))