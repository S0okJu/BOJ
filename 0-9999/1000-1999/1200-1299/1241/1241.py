import sys 

from typing import List 
from collections import deque

input = sys.stdin.readline

def timeout(N:int, students:List[int]):
    """
    - time complexity: O(N^2)
    """
    results = []
    
    for idx, tgt in enumerate(students):
        result = 0
        
        # make queue  
        # O(N)       
        q = deque(students[:idx] + students[idx+1:])
        
        # do head tok tok!
        # O(N-1)
        while q:
            curr = q.popleft()

            if tgt % curr  == 0:
                result += 1
        
        results.append(result)
    
    return results

def solution(N:int, students:List[int]) -> List[int]:     
    max_ = max(students)
    
    freq = [0] * (max_ + 1)
    for student in students:
        freq[student] +=1
    
    # For each number, count how many of its divisors exist
    divisor_cnt = [0] * (max_ + 1)
    
    for divisor, freq_v in enumerate(freq):
        if freq_v > 0:
            # Add this divisor to all its multiples
            for multiple in range(divisor, max_ + 1, divisor):
                divisor_cnt[multiple] += freq_v
    
    # Create new list to return
    return [divisor_cnt[student] - 1 for student in students]
            
if __name__ == '__main__':
    N = int(input())
    students = [int(input().strip()) for _ in range(N)]
    
    results = solution(N=N, students=students)
    for result in results:
        print(result)