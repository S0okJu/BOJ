from collections import deque

import sys 
input = sys.stdin.readline

def solution(N, networks):
    result = 0 
    def bfs(start):
        # variables
        q = deque([])
        visited = [False] * (N+1)
        infected_cnt= 0 
            
        # start point init 
        q.append(start)
        visited[start] = True 

        # count infected computers
        while q:
            curr = q.popleft()
            
            for computer in networks[curr]:
                if not visited[computer]:
                    visited[computer]= True
                    q.append(computer)
                    infected_cnt +=1
        
        return infected_cnt
    
    # 1번 컴퓨터 기준 전염된 컴퓨터 수 구하기
    result = bfs(1)
    return result
            
if __name__ == '__main__':
    computer_cnt = int(input())
    network_pair_cnt = int(input())
    
    networks = [[] for _ in range(computer_cnt + 1)]
    
    for i in range(network_pair_cnt):
        a, b = map(int,input().split())
        networks[a].append(b)
        networks[b].append(a)
    
    print(solution(computer_cnt, networks))
        
