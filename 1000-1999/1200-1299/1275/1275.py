from typing import List
import sys
input = sys.stdin.readline

class BinaryIndexedTree:
    def __init__(self, size: int, nums: List[int]):
        self.size = size
        self.nums = nums.copy()  
        self.tree = [0] * (size + 1)
        self._initialize()

    def _initialize(self):
        """BIT 초기화 메서드"""
        for idx, num in enumerate(self.nums):
            self.update(idx + 1, num)  
            
    def update(self, index: int, value: int):
        """값 누적 업데이트 메서드"""
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def _query(self, index: int) -> int:
        """1부터 index까지의 누적 합 조회"""
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def range_query(self, left: int, right: int) -> int:
        """left부터 right까지 구간 합 계산"""
        return self._query(right) - self._query(left - 1)

if __name__ == '__main__':
    N, Q = map(int, input().split())
    nums = list(map(int, input().split()))
    
    bit = BinaryIndexedTree(N, nums)
    
    for _ in range(Q):
        x, y, a, b = map(int, input().split())
        
        if x > y:
            x, y = y, x
        print(bit.range_query(x, y))
        
        prev_value = bit.nums[a-1]  
        delta = b - prev_value
        bit.update(a, delta)       
        bit.nums[a-1] = b          
