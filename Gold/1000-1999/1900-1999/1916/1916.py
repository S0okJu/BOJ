from heapq import heappop, heappush
from typing import Tuple, List 
import sys 
input = sys.stdin.readline

def solution(N:int, graph:List[List[Tuple[int,int]]], target: Tuple[int,int]) -> int:
    cost = [float('inf')] * (N+1)
    
    target_src, target_dest = target 
    cost[target_src] = 0
    q = [(0, target_src)] 
    
    while q:
        curr_cost, curr_node = heappop(q)
        
        if curr_cost > cost[curr_node]:
            continue
        
        for neighbor, neighbor_cost in graph[curr_node]:
            new_cost = curr_cost + neighbor_cost
            
            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                heappush(q, (new_cost, neighbor))
    
    return cost[target_dest]

if __name__ =='__main__':
    N = int(input())
    M = int(input())
    
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        src, dest, cost = map(int, input().split())
        graph[src].append((dest, cost))

    
    target = tuple(map(int, input().split()))
    print(solution(N, graph, target))
