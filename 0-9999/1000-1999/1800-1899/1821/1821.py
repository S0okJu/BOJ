import sys 
input = sys.stdin.readline

class Solution:
    def __init__(self, N, F):
        self._N = N
        self._F = F
        self._visited = [False] * (N+1)
        self._perm = [0] * 15
        self._arr = [[0] * 15 for _ in range(15)]
    
    def make_permuation(self):
        for i in range(self._N):
            self._arr[0][i] = self._perm[i]
        
        for i in range(1,self._N):
            for j in range(self._N - i):
                self._arr[i][j] = self._arr[i-1][j] + self._arr[i-1][j+1]
        
        return self._arr[self._N - 1][0] == self._F
    
    def backtacking(self, depth):
        if depth == self._N:
            if self.make_permuation():
                print(*self._perm[:self._N])
                sys.exit(0)
            return 
        
        for i in range(self._N):
            if not self._visited[i]:
                self._visited[i] = True 
                self._perm[depth] = i + 1
                
                self.backtacking(depth=depth + 1)
                
                self._visited[i] = False
            
if __name__ == '__main__':
    N, F = map(int,input().split())
    
    solution = Solution(N=N, F=F)
    solution.backtacking(0)