from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, color):
    q= deque([x])
    
    while q:
        now = q.popleft()
        next_color = color[now] % 2 + 1
        
        for n in graph[now]:
            if not color[n]:
                color[n] = next_color
                q.append(n)

            # 인접 노드가 같은 색이라면
            elif color[n] != next_color:
                return False 
    
    return True 
            
if __name__ == '__main__':
    K = int(input())
    
    for i in range(K):
        V, E = map(int,input().split())
        
        graph = [[] for _ in range(V+1)]
        color = [0] * (V+1)
        result = 'YES'
        
        for j in range(E):
            x, y = map(int,input().split())
            graph[x].append(y)
            graph[y].append(x)
        
        for i in range(1, V+1):
            if color[i]:
                continue
            
            # 색칠함 
            color[i] = 1
            
            # 인접한 노드가 색이 같음
            if bfs(i,color) == False:
                result = 'NO'
                break 

        print(result)
