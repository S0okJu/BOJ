from collections import deque
from typing import List

import sys 
input = sys.stdin.readline

def solution(N:int, graph: List[List[int]]) -> List[int]:
    
    parent = [0] * (N+1)
    visited = [False] * (N+1)
    
    def bfs(start:int):
        q = deque([start])
        visited[start] = True 
        
        while q:
            curr = q.popleft()
            
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    parent[neighbor] = curr
                    visited[neighbor] = True
                    q.append(neighbor)     
    bfs(1)
    return parent[2:]
            

if __name__ == '__main__':
    N = int(input())
    
    graph = [[] for _ in range(N+1)]
    graph[1].append(0)
    for n in range(N-1):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = solution(N,graph)
    for val in result:
        print(val)
    