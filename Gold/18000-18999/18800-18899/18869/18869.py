from typing import List
from collections import defaultdict

import sys 
input = sys.stdin.readline

def get_rank(planets:List[int]) -> tuple:
    sorted_planets = sorted(set(planets))    
    rank_map = {v: i for i, v in enumerate(sorted_planets)}
    return tuple(rank_map[v] for v in planets)

def solution(universe:List[List[int]]) -> int:
    rank_count = defaultdict(int)

    for planets in universe:
        rank_tuple = get_rank(planets=planets)
        rank_count[rank_tuple] +=1
    
    count = 0
    for freq in rank_count.values():
        if freq > 1:
            count += freq * (freq-1) // 2 # nC2
    
    return count

if __name__ == '__main__':
    M, N = map(int,input().split())
    
    universe = [list(map(int,input().split())) for _ in range(M)]
    print(solution(universe=universe))

