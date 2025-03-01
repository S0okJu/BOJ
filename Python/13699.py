import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dp = [0] * (n+1)
    dp[0] =1
    
    for i in range(n+1):
        for j in range(i):
            dp[i] += (dp[j] * dp[i-j-1])
    
    print(dp[n])