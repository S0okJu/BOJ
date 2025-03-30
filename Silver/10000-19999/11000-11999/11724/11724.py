import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(node):
    visited[node] = True 
    
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    result = 0 
    
    for _ in range(M):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    
    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)
            result += 1
    
    print(result)