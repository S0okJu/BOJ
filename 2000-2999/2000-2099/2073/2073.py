from typing import List, Tuple 
import sys 
input = sys.stdin.readline

def solution(D:int, pipelines:List[Tuple[int,int]]) -> int:
    dp = [0] * (D+100_001)
    dp[0] = float("inf")
    for length, capacity in pipelines:
        for i in range(D-1, -1, -1):
            if dp[i] > 0:
                dp[i + length] = max(dp[i+length], min(dp[i], capacity))
    
    return dp[D]
    
if __name__ == '__main__':
    D, P = map(int,input().split())
    
    pipelines = list()
    for i in range(P):
        a, b = map(int,input().split())
        pipelines.append((a,b))
    
    print(solution(D,pipelines))