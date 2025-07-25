from typing import List
from collections import Counter

import sys 
input = sys.stdin.readline

def solution(n:int, numbers:List[int]):
    count = Counter(numbers)
    result = []
    
    # counter가 빌 때까지 
    while count:
        # 가장 작은 숫자부터 처리
        min_num = min(count.keys())
        
        # 연속된 숫자 발견 
        if min_num + 1 in count:
            separator = None
            # num + 2 이상의 숫자 찾기 
            for num in sorted(count.keys()):
                if num > min_num + 1:
                    separator = num
                    break
            
            # 결과 배열 바꾸기 
            if separator:
                result.extend([min_num] * count[min_num]) # 같은  숫자들 먼저 배치 
                result.append(separator) # 까워넣기 
                count[separator] -= 1 # 개수 줄이기 
                
                # 다 쓰면 제거하기 
                if count[separator] == 0: 
                    del count[separator] 
            else:
                # 끼워 넣을 숫자가 없으면 순서를 바꿈 
                # 바꾼 숫자를 결과값에 저장하면 카운트도 없애줌 
                result.extend([min_num + 1] * count[min_num + 1])
                result.extend([min_num] * count[min_num])
                del count[min_num + 1]
            
            del count[min_num]
        else: # 연속된 숫자가 아니라면 
            result.extend([min_num] * count[min_num])
            del count[min_num]
    
    print(*result)
    

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int,input().split()))
    
    solution(n=n, numbers=numbers)