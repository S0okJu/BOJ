import sys 
input = sys.stdin.readline

def solution(N:int, M:int, squares)->int:
    result = 1
    diameter = min(N,M)
    
    for d in range(1,diameter+1):
        for x in range(N):
            for y in range(M):
                if x + d >= N or y + d >= M:
                    continue
                # print(f"{d} {x} {y}")
                if squares[x][y] == squares[x+d][y] == squares[x][y+d]==squares[x+d][y+d]:
                    result = max(result, (d+1)**2)
    
    return result
    
if __name__ == '__main__':
    N, M = map(int, input().split())
    
    squares = []
    for i in range(N):
        squares.append(list(map(int,input().strip())))
    
    print(solution(N,M,squares=squares))
        