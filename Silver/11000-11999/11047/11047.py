import sys 
input = sys.stdin.readline

"""
- 문제 : https://www.acmicpc.net/problem/11047
- 조건
    - 동전을 적절히 사용하여 원하는 값을 구함
- 입력
    - 오름 차순으로 동전이 주어짐 
- 출력
    - 필요한 동전 개수의 최솟값
- 시간
    - 웬만한 모든 계산은 다 수행할 수 있음(N 범위가 적음)
"""

def solution(N,K,lst):
    cnt = 0
    
    # 최솟값을 구하기 위해 역으로 수행 
    # 큰 숫자를 우선 많이 사용하는 것이 중요하다. 
    for coin in reversed(lst):
        if K == 0:
            break 
        # 목표치보다 코인의 가격은 적어야 한다.
        if K >= coin:
            cnt += (K // coin)
            K = (K % coin)
    
    return cnt
            
        
if __name__ == '__main__':
    N,K = map(int,input().split())
    lst = []
    
    for i in range(N):
        lst.append(int(input()))
    
    print(solution(N,K,lst))