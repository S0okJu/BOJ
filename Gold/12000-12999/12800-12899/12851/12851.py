from collections import deque
import sys
input = sys.stdin.readline

MAX_N = 100_001

def solution(N, K):
    visitied = [False] * MAX_N
    min_time = MAX_N
    
    cnt = 0
     
    q = deque()   
    q.append((N,0))
    
    while q:
        d, t = q.popleft()
        
        visitied[d] = True
        if d == K:
            if  t == min_time:
                cnt += 1
            elif t < min_time:
                min_time = t
                cnt = 1
            
            
        for i in (d -1, d+1, d *2):
            if 0 <= i < MAX_N:
                if not visitied[i]:
                    q.append((i, t + 1))
                
    
    return min_time, cnt 
            
if __name__ == '__main__':
    N, K = map(int, input().split())
    
    time, methods = solution(N,K)
    
    print(time)
    print(methods)
    