import sys
from typing import List 
input = sys.stdin.readline

def recursion_error(M: int, N: int, K: int, fields: List[List[int]]) -> int:
    visited = [[False for _ in range(N)] for _ in range(M)]

    def dfs(x, y):
        if (x < 0 or x > M-1) or (y < 0 or y >N-1):
            return
        if visited[x][y] or fields[x][y] == 0:
            return
        
        visited[x][y] = True 
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1) 
    
    result = 0 
    for i in range(M):
        for j in range(N):
            if fields[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                result +=1
    
    return result


def solution(M: int, N: int, K: int, fields: List[List[int]]) -> int:
    visited = [[False for _ in range(N)] for _ in range(M)]
    def dfs(x, y):

        stack = [(x,y)]
        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            
            visited[cx][cy] = True 
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx = cx + dx
                ny = cy + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if fields[nx][ny] == 1 and not visited[nx][ny]:
                        stack.append((nx, ny))
        
    result = 0 
    for i in range(M):
        for j in range(N):
            if fields[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                result +=1
    
    return result
             

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        M, N, K = map(int,input().split())
        fields = [[0 for _ in range(N)] for _ in range(M)]
        for _ in range(K):
            x, y = map(int,input().split())
            fields[x][y] = 1
        
        print(solution(M,N,K,fields))