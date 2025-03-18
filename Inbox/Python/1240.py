import sys
from collections import deque
input = sys.stdin.readline



def bfs(start, find):
    # init 
    queue = deque()
    queue.append((start,0))
    visited = [False] * (n+1)
    visited[start] = True
    
    while queue:
        v, d = queue.popleft()
        
        # 찾고자 하는 노드가 일치하다면 
        if v == find:
            return d
        
        for i, l in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i,d + l))
    

n, m = map(int,input().split())    

# 1. init 
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    n1, n2, l = map(int,input().split())
    graph[n1].append((n2, l))
    graph[n2].append((n1,l))

# 2. Want to know
for j in range(m):
    n1, n2 = map(int, input().split())
    print(bfs(n1, n2))
    
