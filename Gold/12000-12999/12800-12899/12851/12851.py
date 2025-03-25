"""
수빈 N
동생 K

수빈 걷기 or 순간 이동
1. 걷기 = (x+1) or (x-1) (1s)
2. 순간 이동 = 2*x (1s)

### output
- 찾을 수 있는 가장 빠른 시간, 방법

"""

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
visited = [False for _ in range(100001)]

def bfs(start):
    # 초기화
    sec = INF
    methods = 0
    q= deque()
    q.append((start,0))
    
    while q:
        d, t = q.popleft()
        visited[d] = True
        
        # 도착지가 같다면 
        # 최소 시간(sec)과 같은 경우에는 경우의 수를 1 증가
        if d == k:
            if t < sec:
                sec = t
                methods = 1
            elif t == sec:
                methods+=1

        # 모든 경우의 수에 대해서 q에 넣는다.
        if 0 <= d+1 <= 100000:
            if not visited[d+1]:
                q.append((d+1, t+1))
        if 0 <= d-1 <= 100000:
            if not visited[d-1]:
                q.append((d-1,t+1))
        if 0 <= 2*d <= 100000:
            if not visited[2*d]:
                q.append((2*d, t+1))

    return sec, methods

s, m = bfs(n)

print(s)
print(m)
                
