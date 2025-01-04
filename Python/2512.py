import sys

def solution():
    n = int(input())
    nums = sorted(list(map(int, sys.stdin.readline().strip().split())))
    m = int(input())
    
    low, high = 0, max(nums)
    
    result = 0 
    while low <= high:
        total = 0
        mid = (low + high)//2
        
        for num in nums:
            total += min(num,mid)
        
        if total <= m:
            low = mid + 1
            result = mid
        else:
            high = mid - 1


    print(result)
if __name__ == '__main__':
    solution()
            