from typing import List

def bitmask(N: int, S: int, numbers: List[int]):
    count = 0
    
    for mask in range(1, 1 << N):
        subset_sum = 0
        for i in range(N):
            if mask & (1 << i):
                subset_sum += numbers[i]
        
        if subset_sum == S:
            count += 1
    
    return count

def solution(N: int, S: int, numbers: List[int]):
    result = 0
    
    def backtracking(index, current_sum, count):
        nonlocal result
        
        if index == N:
            # 크기가 양수이고 합이 S
            if count > 0 and current_sum == S:  
                result += 1
            return
        
        # 현재 원소를 포함하지 않는 경우
        backtracking(index + 1, current_sum, count)
        
        # 현재 원소를 포함하는 경우
        backtracking(index + 1, current_sum + numbers[index], count + 1)
    
    backtracking(0, 0, 0)
    return result
         
if __name__ == '__main__':
    N, S = map(int,input().split())
    numbers = list(map(int,input().split()))
    
    print(solution(N=N, S=S, numbers=numbers))