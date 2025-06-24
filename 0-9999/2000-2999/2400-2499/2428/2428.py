from typing import List 

def solution(N:int, files:List[int]) -> int:
    files.sort()
    
    result = 0
    left = 0
    for right in range(N):
        # left는 전체 for문(즉, 전체 코드)에서 0부터 N-1까지 한 번씩만 증가
        # O(2N) -> 각각 한 방향으로만 움직임
        while left < right and files[left] < 0.9 * files[right]:
            left += 1
        result += (right - left)
    return result
    
if __name__ == '__main__':
    N = int(input())    
    
    files = list(map(int,input().split()))
    
    print(solution(N=N, files=files))
