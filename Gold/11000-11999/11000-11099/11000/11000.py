from typing import List, Tuple

from heapq import heappush, heappop

import sys 
input = sys.stdin.readline

def solution(N:int, lessons: List[Tuple[int, int]]) -> int:
    lessons = sorted(lessons, key=lambda x: x[0])
    classroom = []
    
    for cs,ct in lessons:
        if classroom and classroom[0] <= cs:
            heappop(classroom)
        heappush(classroom,ct)
    
    return len(classroom)
        
        
if __name__ == '__main__':
    N = int(input())
    lessons = []

    for _ in range(N):
        s, t = map(int, input().split())
        lessons.append((s, t))

    print(solution(N, lessons))