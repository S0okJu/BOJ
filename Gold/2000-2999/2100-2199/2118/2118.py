from typing import List 

import sys 
input = sys.stdin.readline

def timeout(N:int, distances:List[int])->int:
    # prefix sum
    sums_ = [0] * (N+1)
    for idx, distance in enumerate(distances):
        sums_[idx+1] = sums_[idx] + distance
        
    
    # 조건에 맞는 거리 구하기
    result = 0 
    for start in range(N):
        shortest = float("inf")
        for end in range(start,N):
            distance = sums_[end]-sums_[start]
            
            shortest = min(distance, sums_[N] - distance)
        
        result = max(result, shortest)
    
    return result

def solution(N:int, distances:List[int])->int:     
    total_ = sum(distances)
    max_segment = 0
    curr_sum = 0
    start = 0
    
    distances += distances
    
    for end in range(N*2):
        curr_sum += distances[end]
        while curr_sum > total_ // 2:
            curr_sum -= distances[start]
            start +=1
        
        max_segment = max(max_segment, curr_sum)
    
    return min(total_ - max_segment, max_segment)

if __name__ == '__main__':
    N = int(input())
    
    distances = []
    for i in range(N):
        distances.append(int(input()))
    
    print(solution(N=N, distances=distances))