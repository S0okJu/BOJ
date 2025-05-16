from typing import List 
from heapq import heappush,heappop
import sys 
input = sys.stdin.readline

def solution(N:int, lessons:List[List[int]]) -> int:
    # 시작 시간을 기준으로 정렬 
    lessons = sorted(lessons, key=lambda x:x[1])
    classrooms = []
    
    for lesson_id, start, end in lessons:
        print(f"{lesson_id}, {start}, {end}")
        if classrooms and classrooms[0][0] <=start:
            print(f"pop {classrooms}")
            heappop(classrooms)
        
        print(f"push {end}")
        heappush(classrooms, (end,lesson_id))
    print(classrooms)
    return len(classrooms)
        
            
        
if __name__ == '__main__':
    N = int(input())
    lessons = [list(map(int,input().split())) for _ in range(N)]
    print(solution(N,lessons))