from collections import deque
from typing import List 
import sys 
from heapq import heappush, heappop
input = sys.stdin.readline

def solution(L:int, S: List[int], n:int) -> List[int]:
    
    S.sort()
    candidate_list = []
    
    # 그룹 1: S에 속하는 수 (f(x)=0)
    for s in S:
        candidate_list.append((0, s))
        
    # 그룹 2: 유한 구간 후보 생성 함수
    def process_gap(L_val, R_val):
        """
        구간 [L_val, R_val] 내 후보들을 (f값, 정수) 튜플로 반환.
        구간의 길이 d = R_val - L_val + 1.
        각 구간에서는 양끝 (L_val, R_val)가 f값이 최소임.
        단, 구간의 길이가 매우 클 수 있으므로 n회(최대 n 라운드)까지만 후보를 생성.
        """
        d = R_val - L_val + 1
        gap_candidates = []
        # 각 라운드는 양쪽에서 하나씩 후보를 선택
        # 라운드 i에서 후보: L_val+i (왼쪽)와 R_val-i (오른쪽)
        # 단, 같은 수가 중복되지 않도록 함.
        rounds = min(n, (d + 1) // 2)
        for i in range(rounds):
            if L_val + i <= R_val - i:
                x_left = L_val + i
                # f(x) = (x - L_val + 1)*(R_val - x + 1) - 1.
                f_val = (i + 1) * (d - i) - 1
                gap_candidates.append((f_val, x_left))
                if L_val + i < R_val - i:
                    x_right = R_val - i
                    gap_candidates.append((f_val, x_right))
        return gap_candidates

    # 왼쪽 유한 구간: [1, S[0]-1] (S의 최솟값이 1보다 크다면)
    if S[0] > 1:
        candidate_list.extend(process_gap(1, S[0] - 1))
        
    # S 사이의 간격에 대하여 후보 생성
    for i in range(len(S) - 1):
        if S[i+1] - S[i] > 1:  # gap이 존재하면
            L_val = S[i] + 1
            R_val = S[i+1] - 1
            candidate_list.extend(process_gap(L_val, R_val))
    
    # 그룹 3: 무한 구간 후보 (S의 최대 원소보다 큰 수)
    # 무한 구간은 f값을 무한(inf)로 처리하며, 오름차순 정렬 시 S[-1]+1, S[-1]+2, ... 순임.
    maxS = S[-1]
    for x in range(maxS + 1, maxS + 1 + n):
        candidate_list.append((float('inf'), x))
    
    # 모든 후보를 (f값, 정수) 기준으로 정렬 (f값이 같으면 정수가 작은 순)
    candidate_list.sort(key=lambda pair: (pair[0], pair[1]))
    
    # 정렬된 전체 후보 중 앞쪽 n개의 정수를 추출
    result = [candidate_list[i][1] for i in range(n)]
    return result

if __name__ == '__main__':
    L = int(input())
    S = list(map(int,input().split()))
    N = int(input())
    
    print(*solution(L,S,N))