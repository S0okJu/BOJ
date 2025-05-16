from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def solve(N):
    # N=0이면 이미 길이가 0이므로 (일수=0, 물=0)
    if N == 0:
        return (0, 0)
    
    # best[length] = (day, water)
    # 길이 length에 도달하는 가장 좋은 방법(day가 가장 작고, 같다면 water가 가장 작은)
    INF = float('inf')
    best = [(INF, INF)] * (N+1)
    
    # 시작 상태: length=0, day=0, water=0
    best[0] = (0, 0)
    pq = []
    heappush(pq, (0, 0, 0))  # (day, water, length)
    
    while pq:
        day, w, length = heappop(pq)
        
        # 만약 이 상태가 best[length]와 다르다면 이미 더 좋은 상태로 방문된 것
        if (day, w) != best[length]:
            continue
        
        # 목표 길이에 도달했으면 즉시 반환
        if length == N:
            return (day, w)
        
        # 다음 날(day+1)로 상태 확장
        nd = day + 1
        
        # 1) length + 1
        nxt_len = length + 1
        if nxt_len <= N:
            nxt_w = w + 1
            # 새 상태가 기존 best[nxt_len]보다 좋은지 확인
            if (nd, nxt_w) < best[nxt_len]:
                best[nxt_len] = (nd, nxt_w)
                heappush(pq, (nd, nxt_w, nxt_len))
        
        # 2) length * 3
        mul3 = length * 3
        if mul3 <= N:
            nxt_w = w + 3
            if (nd, nxt_w) < best[mul3]:
                best[mul3] = (nd, nxt_w)
                heappush(pq, (nd, nxt_w, mul3))
        
        # 3) length^2 (단, length >= 2일 때만 실제로 변화 있음)
        if length >= 2:
            sq = length * length
            if sq <= N:
                nxt_w = w + 5
                if (nd, nxt_w) < best[sq]:
                    best[sq] = (nd, nxt_w)
                    heappush(pq, (nd, nxt_w, sq))

def main():
    N = int(input().strip())
    day, water = solve(N)
    print(day, water)

if __name__ == "__main__":
    main()
