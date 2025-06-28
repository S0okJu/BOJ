from typing import List
import sys
input = sys.stdin.readline

class BinaryIndexedTree:
    def __init__(self, size:int, data:List[int]):
        self.size= size
        self.data = data.copy()
        self.tree = [0] * (size + 1)
        self._initialize()
    
    def _initialize(self):
        """BIT 초기화 메서드"""
        for idx, num in enumerate(self.data):
            self._update(idx + 1, num) 
    
    def _update(self, index:int, value:int):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index
    
    def update(self, index:int, value:int):
        prev = self.data[index - 1]
        delta = value - prev
        self._update(index=index, value=delta)
        self.data[index-1] = value
    
    def _query(self, index:int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        
        return total 

    def range_query(self, left:int, right:int) -> int:
        return self._query(right) - self._query(left - 1)

if __name__ == '__main__':
    N, M, K = map(int,input().split())
    
    data = [int(input().strip()) for _ in range(N)]
    tree = BinaryIndexedTree(size=N, data=data)
    
    for _ in range(M + K):
        a, b, c = map(int,input().split())
        
        if a == 1:
            tree.update(index=b, value=c)
        else:
            print(tree.range_query(left=b, right=c))
    