from typing import List
from collections import defaultdict
import sys 
input = sys.stdin.readline

def solution(N: int, K: int, A: List) -> int:
    sum_ = 0
    result = 0
    sum_map = defaultdict(int)
    sum_map[0] = 1
    for i in range(N):
        sum_ += A[i]    
        result += sum_map[sum_-K]
        sum_map[sum_] +=1
    
    return result
        

if __name__ == '__main__':
    # Input 
    N, K = map(int,input().split())

    A = list(map(int,input().split()))
    
    print(solution(N,K,A))