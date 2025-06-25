from typing import List 


def solution(R: int, C: int, K: int, roads: List[List[str]]) -> int:
    result = 0
    
    def dfs(x: int, y: int, dis: int, visited: List[List[bool]]):
        nonlocal result
        
        if roads[x][y] == 'T' or visited[x][y]:
            return
        
        if dis > K: 
            return

        if x == 0 and y == C - 1:
            if dis == K:
                result += 1
            return
        
        visited[x][y] = True
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                dfs(nx, ny, dis + 1, visited)
        visited[x][y] = False  

    visited = [[False for _ in range(C)] for _ in range(R)]
    dfs(R - 1, 0, 1, visited)
    return result

if __name__ == '__main__':
    R, C, K = map(int, input().split())
    
    roads = []
    for r in range(R):
        roads.append(list(input().strip()))
    
    print(solution(
        R=R,
        C=C,
        K=K,
        roads=roads
    ))
                
