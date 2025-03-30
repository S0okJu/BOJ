import sys 
input = sys.stdin.readline

def solution(numbers, M):
    result = []
    visited = [False] * (len(numbers))
    graph = []
    
    def backtracking(graph):
        if len(graph) == M:
            result.append(graph[:])
            return 

        for n in range(len(numbers)):
            if not visited[n]:
                visited[n] = True 
                graph.append(numbers[n])
                
                backtracking(graph)
                
                visited[n] = False 
                graph.pop()
    
    backtracking(graph)
    return result
                
if __name__ == '__main__':
    # Input
    N, M = map(int,input().split())
    numbers = list(map(int,input().split()))

    numbers.sort()
    
    for r in solution(numbers, M):
        print(*r)