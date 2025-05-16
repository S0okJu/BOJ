from dataclasses import dataclass
from typing import List, Tuple
import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

@dataclass
class Neighbor:
    node: int 
    weight: int 
    
class Solution:
    def __init__(self, N:int):
        self._N = N 
        self._graph: List[List[Neighbor]] = [[] for _ in range(N+1)]
    
    def _prepare(self) -> Tuple[List[bool],List[int]]:
        visited = [False] * (self._N+1)
        distances = [0] * (self._N+1)
        
        return visited, distances
    
    def add(self, start:int, end:int, weight:int):
        self._graph[start].append(Neighbor(end, weight))
        self._graph[end].append(Neighbor(start, weight))
    
    def _dfs(self, node: int, visited: List[bool], distances: List[int]):
        visited[node] = True
        for neighbor in self._graph[node]:
            n_node, n_weight = neighbor.node, neighbor.weight
            if not visited[n_node]:
                distances[n_node] = distances[node] + n_weight
                self._dfs(node=n_node, visited=visited, distances=distances)

    def execute(self) -> int:
        visited, distances = self._prepare()
        self._dfs(node=1, visited=visited, distances=distances)
        farthest = max(range(1, self._N + 1), key=lambda x: distances[x])

        visited, distances = self._prepare()
        self._dfs(node=farthest, visited=visited, distances=distances)

        return max(distances)
        

if __name__ == '__main__':
    N = int(input())

    solution = Solution(N=N)
    for _ in range(N-1):
        a, b, weight = map(int,input().split())
        solution.add(start=a, end=b, weight=weight)
    
    print(solution.execute())