import math
import sys 
input = sys.stdin.readline

def solution(x1:int, y1:int, r1:int, x2:int, y2:int, r2:int) -> int:
    # 두 중심 사이의 거리
    d = math.hypot(x2-x1, y2-y1)
    
    # 두 원이 일치하는 경우(무한히 많은 교점)
    if d == 0 and r1 == r2:
        return -1
    # 교점이 1개(내접 또는 외접)
    elif d == r1 + r2 or d == abs(r1-r2):
        return 1
    # 교점이 2개(서로 다른 두 점에서 만남)
    elif abs(r1-r2) < d < r1 + r2:
        return 2
    else:
        return 0

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        x1,y1,r1,x2,y2,r2 = map(int,input().split())
        print(solution(x1,y1,r1,x2,y2,r2))
        
        