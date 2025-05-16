"""
임의의 등차 간격 계산 O(NM) 까지 계산하여
시간 복잡도는 O(N^3M^3) = O(N^6)이다.
즉 9^6 연산이 수행되므로 2초(4 * 10^7) 내에 가능한 수행 연산보다 적다. 
"""
from math import sqrt
import sys
input = sys.stdin.readline

def is_sqrt(x):
    if int(sqrt(int(x))) ** 2 == int(x):
        return True
    else:
        return False
    
def solution():
    N, M = map(int, input().split())
    # 2차원 배열로 입력 받기
    board = [list(map(int, list(input().strip()))) for _ in range(N)]
    max_square = -1
    
    # 모든 시작점에 대해
    for i in range(N):
        for j in range(M):
            # 행의 공차 (-N부터 N까지)
            for di in range(-N, N):
                # 열의 공차 (-M부터 M까지)
                for dj in range(-M, M):
                    # 공차가 모두 0인 경우는 제외
                    if di == 0 and dj == 0:
                        continue
                        
                    num = ""
                    r, c = i, j
                    
                    # 등차수열을 따라가며 숫자 만들기
                    while 0 <= r < N and 0 <= c < M:
                        num += str(board[r][c])
                        # 현재까지 만든 숫자가 완전제곱수인지 확인
                        current = int(num)
                        if is_sqrt(current):
                            max_square = max(max_square, current)
                        r += di
                        c += dj
    
    print(max_square)

if __name__ == "__main__":
    solution()