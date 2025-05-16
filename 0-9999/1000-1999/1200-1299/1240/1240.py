from typing import List,Tuple
import sys 
input = sys.stdin.readline

def solution(N:int, graph: List[Tuple[int,int]], start:int, end:int)->int:
    visited = [False for _ in range(N+1)]
    result = [0]
    def dfs(start:int, dist:int) -> int :
#         print(dist)
        # 도착 했다면 
        if start == end:
            result[0] = dist
            return
        
        visited[start] = True 
        for neighbor_node, neighbor_dist in graph[start]:
            if not visited[neighbor_node]:
                visited[neighbor_node] = True
                dfs(neighbor_node, dist+neighbor_dist)

    
    dfs(start,0)
    return result[0]
    
if __name__ == '__main__':
    N, M = map(int,input().split())
    
    graph = [[] for _ in range(N+1)]
    for i in range(N-1):
        a,b, dist = map(int,input().split())    
        graph[a].append((b,dist))
        graph[b].append((a,dist))
    
    for j in range(M):
        start, end = map(int,input().split())
        print(solution(N, graph,start,end))