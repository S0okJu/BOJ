import sys 
input = sys.stdin.readline

def solution(N:int, M:int) -> int:

    leaf = 0 
    
    if M == 2:
        leaf = 1
    
    last_leaf = 0 
    for i in range(1, N):
        if M > leaf:
            print(0, i)
            leaf += 1
        else:
            print(last_leaf, i)
        last_leaf = i

if __name__ == '__main__':
    N, M = map(int,input().split())
    
    solution(N=N, M=M)