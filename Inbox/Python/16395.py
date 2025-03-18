import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pascal = [ [0] * (m+1) for _ in range(n+1)]
pascal[1][1] = 1

def solve(n, k):
    for i in range(2,n+1):
        for j in range(1, k+1):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        # print(pascal[i])

solve(n,m)
print(pascal[n][m])
