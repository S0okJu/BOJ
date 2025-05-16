import sys 
input = sys.stdin.readline

def solution(N:int, rgbs: list) -> int:
    for i in range(1,N):
        # i == 0인 경우 
        rgbs[i][0] += min(rgbs[i-1][1],rgbs[i-1][2])
        # i == 1인 경우
        rgbs[i][1] += min(rgbs[i-1][0],rgbs[i-1][2])
        # i == 3
        rgbs[i][2] += min(rgbs[i-1][0],rgbs[i-1][1])
    
    return min(rgbs[N-1])
    

if __name__ == '__main__':
    N = int(input())
    rgbs=[]
    for i in range(N):
        rgb = list(map(int,input().split()))
        rgbs.append(rgb)
        
    print(solution(N, rgbs))
