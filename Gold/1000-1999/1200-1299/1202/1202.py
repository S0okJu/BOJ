import sys; input = sys.stdin.readline
import heapq
from collections import deque

N, K = map(int, input().split())
J = deque(sorted(list(map(int,input().split())) for _ in range(N)))
B = sorted(int(input()) for _ in range(K))

queue = []
answer = 0

# 가방이 정렬된 차례로 살펴본다
for b in B:
    # 아직 뽑지 않는 보석이 남아 있고, 그 중 최소 무게인 보석이 가방에 담긴다면
    while J and J[0][0] <=b:
        # 보석을 뽑아서 
        M, V = J.popleft()
        # 최대 힙 방식으로 queue에 담는다뽑
        heapq.heappush(queue, -V) 
    
    # 가능한 보석이 있다면 하나를 뽑아서 가방에 담는다.
    if queue:
        answer -= heapq.heappop(queue)

print(answer)