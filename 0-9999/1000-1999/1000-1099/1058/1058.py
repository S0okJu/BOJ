from collections import deque
import sys
input = sys.stdin.readline

"""
시간 복잡도 : O(N^3)
"""
def solution(N, friends):
    
    def bfs(idx):
        visited = [False] * (N+1)
        visited[idx] = True 
        # index , count 
        q = deque([(idx,0)])
        count  = 0
        
        while q:
            j, cnt = q.popleft()
            
            # 친구 수가 2보다 크면 안됨
            if cnt >=2:
                continue
            
            for k in range(N):
                if not visited[k] and friends[j][k]:
                    count +=1 
                    q.append((k, cnt+1))
                    visited[k] = True 
        return count 
    
    result = 0
    for i in range(N): 
        result = max(result,bfs(i)) # O(N^2)
    
    return result
    
    
if __name__ == '__main__':
    N = int(input())
    friends =[[0 for _ in range(N)] for i in range(N)]
    for i in range(N):
        f = list(input().rstrip())
        for j in range(N):
            if f[j]  == 'Y':
                friends[i][j] = 1
            
    print(solution(N,friends))