import sys
input = sys.stdin.readline

MAX_N = 10001
def solution():
    """
    조합 방식으로 값을 더해야 함!
    """
    dp = [0] * MAX_N 
    dp[0] = 1
    
    # 1,2,3이 처음에 추가된 경우(사용 가능한 숫자)
    for i in (1,2,3):
        # i ~ MAX_N까지 i를 한번 사용해서 j를 만드는 방법 추가 
        for j in range(i,MAX_N):
            dp[j] += dp[j-i]
    
    return dp

if __name__ == '__main__':
    T = int(input())
    
    dp = solution()
    for i in range(T):
        n = int(input())
        print(dp[n])
        