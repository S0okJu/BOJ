from typing import List,Tuple 
from collections import deque

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

MOVE = [(1,0),(-1,0),(0,1),(0,-1)]

def is_valid_range(N:int, col:int,row:int) -> bool:
    if 0 <= col < N and 0 <= row < N:
        return True
    return False 

def solution(N:int, graph: List[List[int]]) -> Tuple[int,List[int]]:
    visited = [[False for _ in range(N)] for _ in range(N)]
    
                
    def bfs(x,y) -> int :
        work_queue = deque([(x,y)])
        visited[x][y] = True 
        
        # 시작한 것 포함 
        count = 1
        while work_queue:
            curr_x, curr_y = work_queue.popleft()
            
            for dx, dy in MOVE:
                new_x = curr_x + dx
                new_y = curr_y + dy
                
                if not is_valid_range(N,new_x,new_y) or visited[new_x][new_y]:
                    continue
                
                if graph[new_x][new_y] == 1:
                    work_queue.append((new_x, new_y))
                    visited[new_x][new_y] = True
                    count +=1

        return count 
                
    result = []
    for col in range(N):
        for row in range(N):
            # 방문 표시가 되어 있는 경우는 생략
            if visited[col][row]:
                continue
            
            if graph[col][row] ==1:
                cnt = bfs(col,row)
                result.append(cnt)
                
    result_cnt = len(result)
    result.sort()
    return result_cnt, result
            
            

if __name__ == '__main__':
    N = int(input())
    
    graph = []
    for i in range(N):
        graph.append(list(map(int,input().rstrip())))
    
    cnt, lst = solution(N,graph)
    print(cnt)
    for l in lst:
        print(l)
    