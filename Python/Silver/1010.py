
dp = [[0]* 31 for _ in range(31)]

for i in range(1,31):
    dp[0][i] = 1
    dp[i][i] = 1

for i in range(1,30):
    for j in range(1,(30-i)+1):
        
        dp[j][i+j] = dp[j-1][i+j-1]+dp[j][i+j-1]

Tcase =  int(input())
for t in range(Tcase):
    N, M = map(int, input().split())
    print(dp[N][M])
    

                




