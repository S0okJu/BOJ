import sys
input = sys.stdin.readline

def error_timeout(n):
    """ Failed 
    입력 값마다 새로운 dp를 생성하도록 구현 
    
    시간 복잡도 : O(N * T(상수))
    
    !WARNING T의 범위가 확실히 주어지지 않았음.
    !그러나 T가 100이상이라면 시간 초과가 발생할 수 있음  
    """
    dp = [0, 1, 2 ,4]
    
    idx = 4
    while idx <= n:
        v = (dp[idx-1]+dp[idx-2]+dp[idx-3])%1000000009
        dp.append(v)
        #print(dp)
        idx += 1
    
    return dp[n]

MOD = 1_000_000_009
MAX_N = 1_000_000

def solution_fill_dp():
    """ Success 
    dp를 먼저 만든 후 필요한 값을 사용하도록 구현
    시간 복잡도 : O(N)
    """
    
    # 편의를 위해 인덱스를 1부터 시작 
    dp = [0, 1, 2, 4]
    idx = 4 # len(dp)
    
    # dp를 우선 생성 
    while idx <= MAX_N:
        v = (dp[idx-1]+dp[idx-2]+dp[idx-3])%MOD
        dp.append(v)
        idx += 1  
    
    return dp 
    
if __name__ == '__main__':
    # Input Test case 
    T = int(input())
    
    # success 
    dp = solution_fill_dp()
    
    # 각 케이스별로 값 구하기 
    for i in range(T):
        n = int(input())
        print(dp[n])