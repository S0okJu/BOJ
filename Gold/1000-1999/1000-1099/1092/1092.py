import sys
from typing import List 
input = sys.stdin.readline

def solution(N:int, cranes:List, M:int, boxes:List) -> int:
    day = 0
    
    boxes = sorted(boxes,reverse=True)
    cranes = sorted(cranes, reverse=True)
    
    if boxes[0] > cranes[0]:
        return -1 
    
    while boxes:
        for crane in cranes:
            # 현재 크레인보다 최상단의 박스가 더 크다면
            if boxes and crane < boxes[-1]:
                continue
            
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        # 날짜를 업데이트한다.
        day +=1
    
    return day

if __name__ =='__main__':
    N = int(input())
    cranes = list(map(int,input().split()))
    
    M = int(input())
    boxes = list(map(int,input().split()))
    
    print(solution(N,cranes,M,boxes))
