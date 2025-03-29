import sys 
input = sys.stdin.readline

def solution(N):

    N.sort(reverse=True)
    total = 0 
    
    for i in N:
        total += int(i)
    
    if ('0' in N) and ((total%3)==0):
        return ''.join(N)
    
    return -1
    

if __name__ == '__main__':
    N = list(input().strip())
    print(solution(N))