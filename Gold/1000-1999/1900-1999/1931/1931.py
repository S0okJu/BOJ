from typing import List, Tuple 

import sys 
input = sys.stdin.readline

"""
빨리 끝내는 수업을 기준으로 강의실을 사용 = 최대 사용
"""
def solution(N:int, meetings:List[Tuple[int,int]]) -> int:
    # 정렬하기 
    meetings = sorted(meetings, key=lambda x:(x[1], x[0]))
    
    cnt = 0
    last_end_time = 0
    for curr_start, curr_end in meetings:
        
        if last_end_time <= curr_start:
            cnt += 1
            last_end_time = curr_end
        
    return cnt 
        
if __name__ == '__main__':
    N = int(input())
    
    meetings = []
    for i in range(N):
        start, end = map(int,input().split())
        meetings.append((start,end))
    
    print(solution(N,meetings))
                                                                          