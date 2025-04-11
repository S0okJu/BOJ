from typing import List, Tuple 

import sys 
input = sys.stdin.readline

def solution(N:int, schedule: List[Tuple[int,int]]) ->int:
    # 퇴근 시간까지 고려 
    dp = [0 for _ in range(N+1)]
    
    # 역순으로 처리 
    # 인덱스는 0부터 시작 
    for day in range(N-1,-1, -1):
        work_time, price = schedule[day]
        
        new_time = day + work_time
        if new_time <= N:
            # 상담 안한 다음날 vs 상담한 경우 
            dp[day] = max(dp[day+1], price + dp[new_time])
        else:
            # 상담을 안한다.
            dp[day] = dp[day+1]
        
    print(dp)
    return dp[0]
            
             

if __name__ == '__main__':
    N = int(input())
    
    schedule = []
    for day in range(N):
        work_time,price = map(int,input().split())
        schedule.append((work_time,price))
        
    print(solution(N, schedule))