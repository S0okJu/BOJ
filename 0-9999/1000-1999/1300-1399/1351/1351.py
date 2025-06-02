import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def memory_timeout(N:int, P:int, Q:int) -> int:
    # N = 10^12, that's impossible — you'd need petabytes of memory.
    prefix_sum = [0] * (N+1)
    prefix_sum[0] = 1
    for i in range(1,N+1):
        prefix_sum[i] = prefix_sum[i//P] + prefix_sum[i//Q]
    
    # print(prefix_sum)
    
    return prefix_sum[N]

def solution(N:int, P:int, Q:int) -> int:
    memo = {0: 1}

    # 큰 수에서 나누면서 없애는 방법으로 수행 
    def dfs(n):
        if n in memo:
            return memo[n]
        memo[n] = dfs(n // P) + dfs(n // Q)
        return memo[n]

    return dfs(N)

if __name__ == '__main__':
    N, P, Q = map(int,input().split())
    
    print(solution(N=N, P=P, Q=Q))