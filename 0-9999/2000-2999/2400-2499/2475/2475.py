if __name__ == '__main__':
    nums = list(map(int,input().split()))
    
    sum_ = 0
    for num in nums:
        sum_ += num**2
    
    print(sum_%10)
        