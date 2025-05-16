"""
1. 문제 : https://www.acmicpc.net/problem/13549
2. 조건 
    - 1초 : X + 1, X - 1
    - 0초 : 2 * X (순간이동ㄷ
    -> 순간이동하는 경우에는 1초 걸린 것보다 우선 처리되어야 함. 그렇지 않으면 시간이 걸린 데이터를 기반으로 거리가 측정됨(최소값이 되지 않음)
    
"""

import sys 
input = sys.stdin.readline

MAX = 100_001
def timeout(N, K):
    """
    우선순위를 고려하지 않은 경우 
    단순 거리 측정에 의의를 둠
    """
    from collections import deque
    dist = [-1] * MAX
    q = deque()
    q.append(N)
    dist[N] = 0
    
    while q:
        curr_dist = q.popleft()
        
        if curr_dist == K:
            return dist[K]
        
        for nd, cost in ((curr_dist-1, 1),(curr_dist+1,1),(curr_dist*2,0)):
            if 0 <= nd <= 100_000:
                dist[nd] = dist[curr_dist] + cost
                q.append(nd)

from heapq import heappush, heappop

def solution(N,K):
    """
    우선순위 큐를 둬서 우선순위 처리 수행(기본: 최소 힙)
    """
    q= []
    # 시간의 최솟값을 구해야 하기 때문에 기준점을 시간으로 잡는다. 
    heappush(q, (0, N))
    
    time = [float('inf')] * MAX
    time[N] = 0
    
    while q:
        # 시간이 짧은 거리부터 구한다. 
        ct, cd  = heappop(q)
        
        # 중단점, 구하고 하는 값 
        if cd == K:
            return time[K]
        
        # (추가 시간, 거리)를 기준으로 경우의 수 수행
        for nt, nd in ((1, cd +1),(1, cd-1), (0, cd*2)):
            # 새로 추가된 시간(ct, nt)이 현재 시간보다 짧은 경우에만 갱신
            if 0<= nd < MAX and time[nd] > ct + nt: 
                time[nd] = ct + nt
                heappush(q, (ct+nt, nd))


if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solution(N,K))
