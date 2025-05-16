import sys 
input = sys.stdin.readline

def solution(N:int,L:int, W:int, H:int) -> float:
    max_radius = min(L,W,H)
    
    start, end = 0, max_radius
    result = 0.0 
    
    # 100번이면 1e-9 정밀도 충분
    for _ in range(100):
        
        mid = start + (end-start) / 2
        mid_cnt = int(L//mid) * int(W//mid) * int(H//mid)
        
        if mid_cnt < N:
            end = mid    
        else:
            start = mid

        result = start
    return result
            
if __name__ == '__main__':
    N,L,W,H = map(int,input().split())
    print(f"{solution(N,L, W, H):.10f}")