from collections import deque

class TopologySort:
    def __init__(self, n: int):
        self.n = n
        self.graph = [[] for _ in range(n+1)]
        self.indegree = [0] * (n + 1)
    
    def make(self, start:int, end:int):
        self.graph[start].append(end)
        self.indegree[end] += 1
    
    def _work(self):
        result = [1] * (self.n + 1)
        q = deque()
        
        for i in range(1, self.n + 1):
            if self.indegree[i] == 0:
                q.append(i)
            
        while q:
            now = q.popleft()
            
            for next_ in self.graph[now]:
                result[next_] = max(result[next_], result[now] + 1)
                
                self.indegree[next_] -= 1
                if self.indegree[next_] == 0:
                    q.append(next_)
            
        return result[1:]
        
    def solve(self):
        print(*self._work())
        
if __name__ == '__main__':
    N, M = map(int,input().split())
    
    topology = TopologySort(n=N)
    for _ in range(M):
        a, b = map(int,input().split())
        topology.make(start=a, end=b)
        
    topology.solve()
    