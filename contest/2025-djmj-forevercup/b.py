import sys 
input = sys.stdin.readline

def target_x(currx, curry, x, y):
    slope = (curry - y) / (currx - x)
    return x - (y / slope)
    
if __name__ == '__main__':
    W, H = list(map(int,input().split()))
    x, y = list(map(int,input().split()))
    x1, y1, x2,y2 = list(map(int,input().split()))
    
    ax = target_x(x, y, x1, y1)
    by = target_x(x, y, x2, y2)

    # 운동장 벗어날 경우 
    left = max(0, min(ax, by))
    right = min(W, max(ax, by))

    print(f"{left} {right}")
    if left < right:
        print(f"{max(0.0, (right - left) / W):.10f}")  
    else:
        print(f"{max(0.0, (right - left) / W):.10f}")
