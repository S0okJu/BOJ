import sys 
input = sys.stdin.readline

def solution(N:int, r:int, c:int):
    count = 0
    def recursive(size, x, y):
        nonlocal count
        
        # print(f"{size} -> x: {x}, y: {y}")
        if x == r and y == c:
            print(count)
            return 
        
        if size == 1:
            count += 1
            return 
        
        if not (x <= r < x + size and y <= c < y + size):
            # print(f"{x} <= {r} < {x + size} and {y} <= {c} < {y + size}")
            count +=size * size
            return 
        
        recursive(size//2, x, y)
        recursive(size//2, x, y+ size//2)
        recursive(size//2, x + size//2, y)
        recursive(size//2, x+ size//2, y + size//2)
    
    recursive(size=2**N, x=0, y=0)

if __name__ == '__main__':
    N, r, c = map(int,input().split())
    solution(N=N, r=r,c=c)
    
