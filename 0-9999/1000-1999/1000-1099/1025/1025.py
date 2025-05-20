"""
임의의 등차 간격 계산 O(NM) 까지 계산하여
시간 복잡도는 O(N^3M^3) = O(N^6)이다.
즉 9^6 연산이 수행되므로 2초(4 * 10^7) 내에 가능한 수행 연산보다 적다. 
"""
from typing import List 
from math import sqrt
import sys
input = sys.stdin.readline

def is_sqrt(num:int) -> bool :
    if int(sqrt(int(num))) ** 2 == int(num):
        return True 
    return False

def solution(N:int, M:int, board: List[List[int]])->int:
    result = -1 
    for i in range(N):
        for j in range(M):
            for di in range(-N,N):
                for dj in range(-M,M):
                    
                    # di=dj=0인 경우 무한 while문으로 빠지게 됨
                    if di == 0 and dj == 0:
                        continue
                    curr_i, curr_j = i, j
                    num=""
                    
                    while 0 <= curr_i < N and 0 <= curr_j < M:
                        num += str(board[curr_i][curr_j])
                    
                        if is_sqrt(int(num)):
                            result = max(result,int(num))
                        
                        curr_i += di 
                        curr_j += dj 
    
    return result
                        
if __name__ == "__main__":
    N, M = map(int,input().split())
    
    board = []
    for i in range(N):
        board.append(list(map(int,input().strip())))
    print(solution(N=N, M=M, board=board))