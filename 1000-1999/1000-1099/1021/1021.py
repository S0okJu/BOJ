import sys 
input = sys.stdin.readline

from collections import deque

def solution(N,M,targets):
    dq = deque(range(1,N+1))
    
    # 연산 횟수 
    result = 0
    
    # target의 숫자가 나올때까지 회전 
    for target in targets:
        while True:
            if target == dq[0]:
                dq.popleft()
                break
            else:
                # 왼쪽으로 이동
                # 중간값을 기준으로 왼쪽 오른쪽 선별 
                if dq.index(target) <= len(dq)//2:
                    dq.rotate(-1) # 왼쪽 한칸씩 
                    # print(dq)
                    result +=1
                else:
                    # 오른 쪽으로 이동 
                    dq.rotate(1)
                    # print(dq) # 오른쪽 한칸씩 
                    result +=1
    
    return result
                    
if __name__ == '__main__':
    N, M = map(int,input().split())
    targets = list(map(int,input().split()))
    
    print(solution(N,M,targets))
    
