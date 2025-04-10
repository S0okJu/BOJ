from heapq import heappush, heappop
from typing import List, Tuple 

import sys 
input = sys.stdin.readline

def solution(N:int, lectures:List[Tuple[int,int,int]]) -> int:
    # 시작, 끝을 시점으로 정렬 
    lectures = sorted(lectures, key=lambda x:(x[1],x[2]))
    
    empty_classroom = []
    for i in range(1,N+1):
        heappush(empty_classroom,i)
    
    # (end, classroom_id)
    work_heap = []
    
    result = [0 for _ in range(N+1)]
    
    for lecture in lectures:
        lec_id, start,end = lecture
        
        while work_heap and work_heap[0][0] <= start:
            _, out_classroom= heappop(work_heap)
            heappush(empty_classroom, out_classroom)
        
        in_use_room = heappop(empty_classroom)
        result[lec_id] = in_use_room
        heappush(work_heap,(end, in_use_room))
        
        
    print(max(result))
    for x in result[1:]:
        print(x)
        
if __name__ == '__main__':
    N = int(input())
    
    lectures = []
    for _ in range(N):
        lec_id, start, end = map(int, input().split())
        lectures.append((lec_id,start, end))
    
    solution(N,lectures)