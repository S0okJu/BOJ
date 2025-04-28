import math 
import sys
input = sys.stdin.readline

def find_n_from_sum(total_sum):
    discriminant = 1 + 8 * total_sum
    if discriminant < 0:
        return None  # 해가 없음
    n = (-1 + math.isqrt(discriminant)) // 2
    return n

if __name__ == '__main__':
    S = int(input())
    print(find_n_from_sum(S))
    
    