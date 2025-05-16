from typing import List
import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solution(n:int,w:int,  graph:List[List[int]]) -> float:   
    visited = [False] * (n+1)
    cnt = 0 
    stack = [1]
    visited[1] = True 
    
    while stack:
        node = stack.pop()
        children= 0
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                children+=1
                visited[neighbor] = True
                stack.append(neighbor)
        
        if children == 0:
            cnt+=1
        
    return w/cnt
                

if __name__ == '__main__':
    n, w = map(int,input().split())    
    graph = [[]for _ in range(n+1)]    
    
    for _ in range(n-1):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    print(solution(n=n, w=w, graph= graph))    
        