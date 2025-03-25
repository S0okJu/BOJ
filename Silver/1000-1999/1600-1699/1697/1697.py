from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int,input().split())
    q = deque()
    
    dist = [0] * 100_001
    
    q.append(N)
    
    while q:
        curr = q.popleft()
        
        if curr == K:
            print(dist[K])
            break 
        for i in (curr -1, curr+1, curr * 2):
            if 0 <= i <= 100_000 and not dist[i]:
                dist[i] = dist[curr] + 1
                q.append(i)  