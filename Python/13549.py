from heapq import heappush, heappop


def dijkstra(start):
    q = []		
    heappush(q, (0, start))	

    time = [-1] * MAX	
    time[start] = 0	# 시작 위치의 가중치는 항상 0

    while q:
        t, cx = heappop(q)
        if cx == k:
            return time[cx]

        for i in range(3):
            if i == 0:
                nx = cx - 1
            elif i == 1:
                nx = cx + 1
            else:
                nx = cx * 2

            if not 0 <= nx < MAX:			  
                continue
            if time[nx] != -1 and time[nx] <= time[cx]: 
                continue				  

            if i < 2:			
                heappush(q, (time + 1, nx))
                time[nx] = time + 1
            else:	
                heappush(q, (time, nx))
                time[nx] = time


n, k = map(int, input().split())
MAX = 100001
print(dijkstra(n))