import sys 
input = sys.stdin.readline

def solution(N):
    dp = [float('inf')] * (N+1)
    dp[N] = 0
    
    for n in range(N, 0, -1):
        # 특별한 조건이 없으므로 우선 값 처리 
        dp[n-1] = min(dp[n] + 1, dp[n-1])
        if n % 3 == 0:
            dp[n//3] = min(dp[n//3],dp[n] + 1)
        if n % 2 == 0:
            dp[n//2] = min(dp[n//2],dp[n] + 1)
    # print(dp[:N])  
    return dp[1]         

if __name__ == '__main__':
    N = int(input())
    print(solution(N))