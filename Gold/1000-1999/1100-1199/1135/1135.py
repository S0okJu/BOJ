from collections import deque
from typing import List 
import sys 
input = sys.stdin.readline



def solution(N:int, graph: List[List[int]]) -> int:
    
    def dfs(node:int) -> int:
        times = []
        
        for child in graph[node]:
            times.append(dfs(child))
        
        # 오래 걸리는 순서대로 정렬해서 전화해야 시간 단축 가능
        times.sort(reverse=True)
        # 자식이 많고, 오래 걸리는 자식이 뒤에 있을수록 max_time이 계속 커져요.
        max_time = 0
        for order, time_taken in enumerate(times):
            # 가장 오래 걸리는 경로가 즉 부모의 완료 시간이다. 
            max_time = max(max_time, time_taken + order + 1)
        
        return max_time
    
    result = dfs(0)
    return result
    
if __name__ == '__main__':
    N = int(input())
    bosses = list(map(int,input().split()))
    
    graph = [[] for _ in range(N)]
    for staff, boss in enumerate(bosses):
        if boss == -1:
            continue
        graph[boss].append(staff)
        
    print(solution(N,graph))