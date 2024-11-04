import heapq

def dijkstra(start):
    q = []
    # 시작 노드 큐에 넣기
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        # 이미 처리된 경우
        # 최단거리를 구하는 것이기 때문에 dist보다 작으면 조건에 이미 만족한 것이라고 판단
        if distance[now] < dist:
            continue

        # 인접 노드 확인
        for pos, c in bus[now]:
            cost = dist + c

            # 최솟값 구하기 
            if cost < distance[pos]:
                distance[pos] = cost
                heapq.heappush(q, (cost, pos))

N = int(input())
M = int(input())

bus = [[] for _ in range(N+1)]
distance = [int(1e9)] * (N+1)
for _ in range(M):
    a, b, cost = map(int, input().split())
    bus[a].append((b, cost))

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])