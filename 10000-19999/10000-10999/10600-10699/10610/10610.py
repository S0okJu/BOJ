import sys 
input = sys.stdin.readline

def solution(N):

    N.sort(reverse=True)
    total = 0 
    
    for i in N:
        total += int(i)
    
    # 30의 배수의 마지막은 무조건 0이 있어야 함
    # 3의 배수가 되려면 모든 값의 합이 3이여야 함
    if ('0' in N) and ((total%3)==0):
        return ''.join(N)
    
    return -1
    
if __name__ == '__main__':
    N = list(input().strip())
    print(solution(N))