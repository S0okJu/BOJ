
def solution(N:int) -> int:
    
    turn = 1 
    while True:
        
        if N > 3:
            N-=3
        else:
            N-=1
        
        if N == 0:
            return 'SK' if turn%2 ==1 else 'CY'
        
        turn += 1
        
if __name__ == '__main__':
    N = int(input())
    print(solution(N=N))