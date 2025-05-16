import sys
sys.setrecursionlimit(10**6)

def dfs(node, graph, visited, distances):
    visited[node] = True
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            distances[neighbor] = distances[node] + weight
            dfs(neighbor, graph, visited, distances)


def solution():
    # Input 
    v = int(input())
    
    # input as graph 
    graph = [[] for i in range(v+1)]
    visited = [False] * (v+1)
    distances = [0] * (v+1)
    
    for _ in range(v):
        temp = list(map(int, sys.stdin.readline().strip().split()))
        start = temp[0]
        for i in range(1, len(temp)-1, 2):
            graph[start].append((temp[i],temp[i+1]))
    
    # 가장 먼 노드 
    dfs(1, graph, visited, distances)
    u = max(range(1, v+1), key=lambda x: distances[x])
    
    visited = [False] * (v+1)
    distances = [0] * (v+1)
    
    # 다시 탐색 
    dfs(u, graph, visited, distances)
    v = max(range(1, v+1), key= lambda x: distances[x])
    print(distances[v])

if __name__ == '__main__':
    solution()
    