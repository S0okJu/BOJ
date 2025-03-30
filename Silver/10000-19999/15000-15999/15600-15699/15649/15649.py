import sys
input = sys.stdin.readline

def permutation(N, M):
    
    result = []
    visited = [False] * (N+1)
    graph = []
    def backtracking(graph):
        
        # 배열 깊이에 따라 break
        if len(graph) == M:
            result.append(graph[:])
            return 
        
        for i in range(1,N+1):
            if not visited[i]:
                visited[i] = True
                graph.append(i)
                
                backtracking(graph)
                graph.pop()
                visited[i] = False 
    
    backtracking(graph)
    return result
            

if __name__ == '__main__':
    N, M = map(int,input().split())
    for p in permutation(N,M):
        print(*p)
