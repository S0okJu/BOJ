from typing import List
from collections import defaultdict

import sys 
input = sys.stdin.readline

def solution(N:int, S:int, nums: List[int]) -> int:
    sums_dict = defaultdict(int)   
    cnt = 0
    
    def left(start, sums):
        if start == N // 2:
            sums_dict[sums] += 1
            return 
        
        left(start=start + 1, sums=sums)
        left(start=start + 1, sums=sums + nums[start])
    
    def right(mid, sums):
        nonlocal cnt 
        
        if mid == N:
            if sums_dict[S-sums]:
                cnt += sums_dict[S-sums]
            return 
        
        right(mid=mid + 1, sums=sums)
        right(mid=mid + 1, sums=sums+nums[mid])
        
    left(0,0)
    right(N//2,0)
    
    return cnt if S else cnt - 1

if __name__ == '__main__':
    N, S = map(int,input().split())
    nums = list(map(int,input().split()))
    
    print(solution(N=N, S=S, nums=nums))
