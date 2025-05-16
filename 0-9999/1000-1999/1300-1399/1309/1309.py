import sys 
input = sys.stdin.readline

def solution(N: int) -> int:
    # (N+1) * 3 metrix 제작 
    # dp[라인 수][사자가 배치되는 위치]
    # 0 ~ 3 : 사자가 배치되는 위치 
    dp = [[1 for _ in range(3)] for _ in range(N+1)]
    
    for i in range(2, N+1):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) %9901
    # print(dp)
    return sum(dp[N])% 9901
    
if __name__ == '__main__':
    N = int(input())
    print(solution(N))
