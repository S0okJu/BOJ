from typing import List 

import sys 
input = sys.stdin.readline

def convert_int(score:str) -> int:
    int_part, frac_part = score.split('.') 
    return (int(int_part) * 1000) + int(frac_part)

def possible(n: int, score:List[int]) -> bool:
    for score in scores:
        r = (score * n) % 1000          
        if r != 0 and 1000 - r >= n: 
            return False
    return True

def solution(N: int, scores: list[str]) -> int:
    for n in range(1, 1001):
        if possible(n, scores):
            return n 
           
if __name__ == '__main__':
    N = int(input())
    scores = [convert_int(input().strip()) for _ in range(N)]
    
    print(solution(N,scores))
