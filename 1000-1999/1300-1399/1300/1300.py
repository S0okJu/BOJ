import sys 
input = sys.stdin.readline

def solution(N:int,K:int) -> int:
    # K번째 수는 K보다 클 수 없음
    start, end = 1, K
    result = 0    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in range(1,N+1):
            # N을 초과하지 않은 수
            count += min((mid // i),N)
        
        if K <= count:
            result = mid
            end = mid -1
        else:
            start = mid + 1
            
    return result
        

if __name__ == '__main__':
    N = int(input())
    K = int(input())
    print(solution(N,K))