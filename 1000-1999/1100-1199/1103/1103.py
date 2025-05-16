from typing import List 
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def solution(N:int, M:int, graph: List[List[str]]) -> int:
    move = [(-1,0), (0,1), (1,0), (0,-1)]
    dp = [[0] *M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    is_cycle = [False]   # 싸이클 발생 여부
    
    def dfs(x, y):
        # 범위가 벗어나는 경우     
        if x < 0 or x >= N or y < 0 or y >= M:
            return 0
        
        # 구멍인 경우 
        if graph[x][y] == 'H':
            return 0 

        if visited[x][y]:
            is_cycle[0] = True
            return 0
            
        if dp[x][y]:
            return dp[x][y]
    
        visited[x][y]= True 
        max_count = 0
        steps = int(graph[x][y])
        for dx, dy in move:
            nx, ny = x + dx * steps, y + dy * steps
            result = dfs(nx,ny)
            max_count = max(max_count,result)
        visited[x][y] = False 
        dp[x][y] = max_count +1
        return dp[x][y]
    
    result = dfs(0,0)
    # print(is_cycle)
    return -1 if is_cycle[0] else result

        

if __name__ == '__main__':
    N, M = map(int,input().split())
    graph = []
    
    for i in range(N):
        row = list(input().strip())
        graph.append(row)
    
    print(solution(N,M,graph))