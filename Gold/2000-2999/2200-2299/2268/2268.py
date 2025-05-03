from typing import List
import sys
input = sys.stdin.readline

class BinaryIndexedTree:
    def __init__(self, size:int):
        self.size = size
        self.nums = [0] * (size+1) 
        self.tree = [0] * (size + 1)

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
    N, M = map(int, input().split())
    
    bit = BinaryIndexedTree(N)
    
    results = []
    for _ in range(M):
        func, a, b= map(int, input().split())
        
        if func == 0:
            if a > b:
                a, b = b, a
            results.append(bit.range_query(left=a, right=b))
        else:
            prev_value = bit.nums[a-1]  # 원본 배열은 0-based
            delta = b - prev_value
            bit.update(a, delta)       # BIT는 1-based 인덱스 사용
            bit.nums[a-1] = b          # 원본 배열 갱신

    for result in results:
        print(result)