def calc(inp):
    return sum(inp[i] * (10 ** (i - 1)) for i in range(1, 5))

def sv(n, t, N, M, dp):
    if t >= M:
        return int(n > N)
    if dp[n][t] >= 0:
        return dp[n][t]
    
    inp = [0] * 5
    tmp = n
    for i in range(1, 5):
        inp[i] = tmp % 10
        tmp //= 10
    
    ret = 1 - (t % 2)
    for i in range(1, 5):
        inp[i] = (inp[i] + 1) % 10
        if sv(calc(inp), t + 1, N, M, dp) == (t % 2):
            ret = t % 2
        inp[i] = (inp[i] - 1 + 10) % 10
    
    dp[n][t] = ret
    return ret

def solve(N, M):
    dp = [[-1] * (M + 2) for _ in range(10000)]  # M + 2 크기로 변경
    return "koosaga" if sv(N, 1, N, M, dp) else "cubelover"

# 입력 처리
N, M = map(int, input().split())
print(solve(N, M))