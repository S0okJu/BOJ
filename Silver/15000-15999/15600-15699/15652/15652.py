import sys 
input = sys.stdin.readline

def solution(N, M):
    result = []
    graph = []
    
    def backtracking(graph):
        if len(graph) == M:
            result.append(graph[:])
            return 
        
        for i in range(1, N + 1):
            before = graph[-1] if graph else 0 
            if before <= i :
                graph.append(i)
                backtracking(graph)
                graph.pop()
    
    backtracking(graph)
    return result 
                
if __name__ == '__main__':
    # Input 
    N, M = map(int, input().split())
    
    for r in solution(N,M):
        print(*r)
