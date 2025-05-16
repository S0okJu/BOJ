from typing import List
import sys 
input = sys.stdin.readline


def solution(N:int, price:List[int], ready_price:int) -> int:
    
    # N = 1일 경우 0만 구매할 수 있음
    if N == 1:
        return 0
     
    # (가격, 방 번호) 형태로 변환 
    nonzero_room = [(price[x],x) for x in range(1,N)]
    nonzero_min_cost, nonzero_room_num = min(nonzero_room, key=lambda x:x[0])
    
    # price 중 최소 비용 찾기
    min_cost = min(price)
    min_idx = price.index(min_cost)
    
    # 첫 자리를 nonzero_room_num을 사용 
    count = (M - nonzero_min_cost) // min_cost + 1
    result = [None] * count
    result[0] = nonzero_room_num
    for i in range(1,count):
        result[i] = nonzero_room_num
        
    # 사용한 비용 계산
    cost_used = nonzero_min_cost + (count - 1) * min_cost
    leftover = M -cost_used
    
    # 숫자 업그레이드
    for i in range(count):
        base_cost = nonzero_min_cost if i==0 else min_cost
        
        for d in range(N, -1,-1,-1):
            if i ==0 and d == 0:
                continue
            
            diff = price[d] - base_cost
            if diff < leftover:
                # 최대 값으로 업데이트
                if d > result[i]:
                    result[i] = d
                    leftover -= diff
                    break 
                    
    
    return int(''.join(map(str,result)))


if __name__ == '__main__':
    N = int(input())
    price = list(map(int,input().split()))
    M = int(input())
    print(solution(N,price,M))