import sys 
input = sys.stdin.readline

def solution(N, M, lst):
    result = []
    graph = []
    visited = [False] * (N+1)
    
    lst.sort()
    
    def backtracking(graph):
        if len(graph) == M:
            result.append(graph[:])
            return 
        
        for i in range(N):
            last = graph[-1] if graph else 0
            if last < lst[i] and not visited[i]:
                visited[i] = True 
                graph.append(lst[i])
                
                backtracking(graph)
                
                graph.pop()
                visited[i] = False 

    backtracking(graph)
    return result 
if __name__ == '__main__':
    N, M = map(int, input().split())
    n_lst = list(map(int,input().split()))
    
    for r in solution(N,M,n_lst):
        print(*r)
