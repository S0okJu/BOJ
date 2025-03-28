import sys 
input = sys.stdin.readline

def solution(A, lst):
    dp = [1] * 1_001
    
    # 끝 번호를 기준으로 차근차근 dp를 채워야 함
    for i in range(A):
        for j in range(i):
            if lst[i] < lst[j]:
                dp[i] = max(dp[j] + 1, dp[i])
        
    return max(dp)
          
if __name__ == '__main__':
    A = int(input())
    lst = list(map(int,input().split()))

    print(solution(A, lst))
