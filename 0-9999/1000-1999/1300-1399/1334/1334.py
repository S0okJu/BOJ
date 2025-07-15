import sys
input = sys.stdin.readline

def is_palindrome(n):
    return n == n[::-1]

def solution(n:int):
    n += 1
    s = str(n)
    len_ = len(s)
    mid = (len_ + 1) // 2
    
    if is_palindrome(s):
        return s
    
    # 펠렌드롬이 n보다 클 경우     
    left_half = s[:mid]
    cand = None 
    if len_ % 2 == 0:
        cand = left_half + left_half[::-1]
    else:
        cand = left_half + left_half[-2::-1]
    
    if int(cand) > n:
        return cand
    
    # 펠렌드롬이 n보다 커 숫자를 증가시켜야 할 경우 
    left_half_up = str(int(left_half) + 1)
    if len(left_half_up) > len(left_half):
        return '1' + '0' * (len_ - 1) + '1'
    
    result = None 
    if len_ % 2 == 0:
        result = left_half_up + left_half_up[::-1]
    else:
        result = left_half_up + left_half_up[-2::-1]
    return result
        

if __name__ == '__main__':
    n = int(input().strip())
    print(solution(n))
