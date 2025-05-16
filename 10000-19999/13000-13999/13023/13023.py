import sys
input = sys.stdin.readline

N, M = map(int, input().split())

relationship = [[] for _ in range(N)]
visited = [False] * N
result = 0

def dfs(x, depths):
    global result
    if depths == 4:
        result = 1
        return 
    
    for i in relationship[x]:
        if not visited[i]:
            visited[i] = True 
            dfs(i, depths + 1)
            visited[i] = False
    
if __name__ == '__main__':

    for _ in range(M):
        a, b = map(int, input().split())
        relationship[a].append(b)
        relationship[b].append(a)
    
    for i in range(N):
        visited[i] = True 
        dfs(i,0)
        visited[i] = False
        
        if result == 1:
            break 
    
    print(result)
        
