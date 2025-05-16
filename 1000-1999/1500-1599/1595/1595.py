import sys 
from collections import deque 
input = sys.stdin.readline

def bfs(x):
    visited[x] = 0
    q = deque([x])
    
    while q:
        x = q.popleft()
        for i, w in graph[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + w
                q.append(i)


graph = [[] for _ in range(10001)]
while True:
    try:
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a,w))
    except:
        break 

visited = [-1 for _ in range(10001)]
bfs(1)
s = visited.index(max(visited))

# 새로운 방문
visited = [-1 for _ in range(10001)]
bfs(s)
print(max(visited))