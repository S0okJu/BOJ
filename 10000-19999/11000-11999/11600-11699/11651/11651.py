import sys 
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int,input().split())
    nums = list(map(int,input().split()))
    
    prefix_sum = [0] * (N+1)   
    sum_ = 0
    for idx, num in enumerate(nums):
        sum_ += num
        prefix_sum[idx+1] = sum_
    
    for request in range(M):
        i, j = map(int,input().split())
        print(prefix_sum[j] - prefix_sum[i-1])
    
        
        
