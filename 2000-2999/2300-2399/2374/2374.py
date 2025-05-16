from typing import List 

import sys 
input = sys.stdin.readline


def solution(N:int, A: List[int])->int:
    result = 0
    stack = []
    target = 0 
        
    for a in A:
        target = max(target, a)
        
        if stack:
            top = stack[-1]
            if top < a:
                result +=(a-stack.pop())
            else:
                stack.pop()

        
        stack.append(a)
    
    while stack:
        result += (target-stack.pop())
        
    return result
            
        
if __name__ == '__main__':
    N = int(input())
    
    A = []
    for i in range(N):
        A.append(int(input()))
        
    print(solution(N=N, A=A))
