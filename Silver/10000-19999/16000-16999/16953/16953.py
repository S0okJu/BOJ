from collections import deque
import sys 
input = sys.stdin.readline

MAX = 1_000_000_000
def solution(A, B):
    
    q = deque()
    q.append((A,0))

    while q:
        curr_n, curr_cnt = q.popleft()
        
        if curr_n == B:
            return curr_cnt + 1
        
        for i in (curr_n * 2, (curr_n * 10)+1):
            if 1 <= i <= MAX and i <= B:
                # print(f"i: {i}")
                q.append((i, curr_cnt +1))
    
    return -1
                    

if __name__ == '__main__':
    A, B = map(int,input().split())
    print(solution(A,B))
