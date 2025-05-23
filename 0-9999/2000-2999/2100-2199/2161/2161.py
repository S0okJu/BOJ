from collections import deque
import sys 
input = sys.stdin.readline

def solution(N:int) -> list:
    queue = deque([n for n in range(1,N+1)])
    remainder = []
    
    while queue:
        first = queue.popleft()
        remainder.append(first)
        
        if len(queue) > 1:
            second = queue.popleft()
            queue.append(second)
    
    return remainder
        
if __name__ == '__main__':
    N = int(input())
    print(*solution(N=N))