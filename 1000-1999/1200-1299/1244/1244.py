from typing import List 

import sys 
input = sys.stdin.readline

MALE = 1
FEMALE = 2

ON = 1
OFF = 0

def solution(swicthes_cnt:int, switches:List[int], students:List[int])-> List[int]:
    
    def convert(target:int):    
        if switches[target] == ON:
            switches[target] = OFF
        else:
            switches[target] = ON
    
    for sex, received in students:
        if sex == MALE:
            # 배수만큼
            for target in range(received-1,swicthes_cnt,received):
                convert(target)
        else:
            idx = received - 1
            convert(idx)  # 중심 먼저 토글

            left = idx - 1
            right = idx + 1
            
            while left >= 0 and right < switches_cnt and switches[left] == switches[right]:
                convert(left)
                convert(right)
                left -= 1
                right += 1
            
    
    return switches
                
def chunk_list(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]
                
if __name__ == '__main__':
    switches_cnt = int(input())
    switches = list(map(int,input().split()))
    
    students_cnt = int(input())
    students = []
    for i in range(students_cnt):
        a, b = map(int,input().split())
        students.append((a,b))
    
    result = solution(switches_cnt, switches, students)
    
    for chunk in chunk_list(result,20):
        print(*chunk)