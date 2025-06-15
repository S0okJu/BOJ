
def solution(N:int) -> int :
    s= ''.join(str(i) for i in range(1,N+1))
    pos = s.find(str(N)) + 1
    
    return pos 

if __name__ == '__main__':
    N = int(input())
    print(solution(N))