from typing import List, Tuple 
from heapq import heappush, heappop

import sys 
input = sys.stdin.readline

def solution(V:int, graph:List[Tuple[int,int]], start:int) -> List[int]:
    distance = [float('inf')] * (V + 1)
    distance[start] = 0
    q = [(0, start)]
    
    while q:
        curr_weight, curr_node = heappop(q)
        
        if curr_weight > distance[curr_node]:
            continue
        
        for neighbor, neighbor_weight in graph[curr_node]:
            new_weight = curr_weight + neighbor_weight
            if new_weight < distance[neighbor]:
                distance[neighbor] = new_weight
                heappush(q, (new_weight, neighbor))
    
    return distance[1:]
    
    
if __name__ == '__main__':
    V, E = map(int,input().split())
    start = int(input())
    
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        src, dest, weight = map(int,input().split())
        graph[src].append((dest,weight))
    
    
    results = solution(V, graph,start)
    for result in results:
        if result == float('inf'):
            print("INF")
        else:
            print(result)
        
        