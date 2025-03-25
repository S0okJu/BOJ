import sys 
input = sys.stdin.readline

def solution(N, M):
    result = []
    visited = [False] * (N + 1)
    graph = []
    
    def backtracking(graph):
        if len(graph) == M:
            result.append(graph[:])
            return 
        
        for i in range(1,N+1):
            if not visited[i]:
                # print(graph)
                last = graph[-1] if graph else 0
                if last < i:
                    visited[i] = True
                    graph.append(i)
                    
                    backtracking(graph)
                    
                    graph.pop()
                    visited[i] = False 
        
    backtracking(graph)
    return result
                        

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    results = solution(N,M)
    for result in results:
        print(*result)