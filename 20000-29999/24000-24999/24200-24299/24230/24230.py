from typing import List
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class ColoredTree:
    def __init__(self, N: int, wanted: List[int], graph: List[List[int]]):
        self._N = N
        self._wanted = wanted
        self._graph = graph
        self._visited = [False] * (N+1)
        self._cnt = 0

    def _dfs(self, node:int, parent_color:int):
        curr_color = self._wanted[node-1]
        
        if curr_color != 0 and curr_color != parent_color:
            self._cnt +=1
            
        self._visited[node] = True 
        for neighbor in graph[node]:
            if not self._visited[neighbor]:
                new_color = curr_color if curr_color !=0 else parent_color
                self._dfs(node=neighbor, parent_color=new_color)
    
    def solution(self) -> int:
        self._dfs(1,0)
        return self._cnt


if __name__ == '__main__':
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    wanted = list(map(int, input().split()))

    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    tree = ColoredTree(N=N, wanted=wanted, graph=graph)
    print(tree.solution())
