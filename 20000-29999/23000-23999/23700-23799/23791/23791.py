from typing import List,Tuple 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

def solution(A:List[int], B:List[int], i:int, j:int, k:int) -> Tuple[int,int]:
    
    # A에서 고를 수 있는 최소 개수 
    left = max(0, k - j)
    # A에서 고를 수 있는 최소 개수 
    right = min(k, i)

    while left <= right:
        print(f"{left}, {right}")
        a_cnt = (left + right) // 2
        b_cnt = k - a_cnt

        # 안전하게 경계 처리
        a_left = A[a_cnt - 1] if a_cnt > 0 else -float('inf')
        b_left = B[b_cnt - 1] if b_cnt > 0 else -float('inf')

        a_right = A[a_cnt] if a_cnt < i else float('inf')
        b_right = B[b_cnt] if b_cnt < j else float('inf')
        print(f"{a_left}, {b_left}, {a_right}, {b_right}")        
        if a_left <= b_right and b_left <= a_right:
            # k번째 원소는 a_left와 b_left 중 큰 값
            if a_left >= b_left:
                return 1, a_cnt  
            else:
                return 2, b_cnt 
        elif a_left > b_right:
            right = a_cnt - 1
        else:
            left = a_cnt + 1

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Q = int(input())

    for _ in range(Q):
        i, j, k = map(int, input().split())
        food_type, idx = solution(A, B, i, j, k)
        print(food_type, idx)
