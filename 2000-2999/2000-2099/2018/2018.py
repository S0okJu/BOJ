from typing import List 

import sys 
input = sys.stdin.readline

def solution(N:int) -> int:
    count = 0
    k = 1
    while k * (k + 1) // 2 <= N:
        if (N - (k*(k-1) //2)) % k == 0:
            count += 1
        k +=1
    return count
            
if __name__ == '__main__':
    N = int(input())
    print(solution(N=N))