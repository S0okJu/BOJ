import sys 
input = sys.stdin.readline

def solution(N, graph) -> int:
   
    def dfs(start):
        visited = [False] * (N+1)
        stack = [start]
        cnt = 0
        while stack:
            v = stack.pop()
            
            if not visited[v]:
                visited[v] = True
                cnt +=1
                stack.append(graph[v])
        
        return cnt 
    
    max_ = 0
    result = N+1
    for i in range(1, N+1):
        cnt = dfs(i)
        if (cnt == max_ and i < result) or cnt > max_:
            max_ = cnt
            result = i
    return result
            
        
if __name__ == '__main__':
    N = int(input())
    
    graph = [0]
    for i in range(N):
        graph.append(int(input()))
        
    print(solution(N,graph))