from sys import stdin

def dfs(a,b,c, prev):
    # stop 
    if [a,b,c] == cnt:
        print(''.join(answer))
        exit(0)
    
    if dp[a][b][c][prev[0]][prev[1]]:
        return False
    
    dp[a][b][c][prev[0]][prev[1]] = True 
    
    if a + 1 <= cnt[0]:
        answer[a+b+c] = 'A'
        if dfs(a+1, b, c, [prev[1],0]):
            return True
    
    if b + 1 <= cnt[1]:
        answer[a+b+c] = 'B'
        if prev[1] != 1:
            if dfs(a, b+1, c, [prev[1],1]):
                return True
    
    if c + 1 <= cnt[2]:
        answer[a+b+c] = 'C'
        if prev[0] != 2 and prev[1] != 2:
            if dfs(a, b, c+1, [prev[1],2]):
                return True
    
    return False

if __name__ == '__main__':
    s = list(stdin.readline().rstrip())
    length = len(s)
    answer = [''] * length
    
    cnt = [s.count(word) for word in ('A','B','C')]
    dp =[[[[[False for _ in range(3)] for _ in range(3)] for _ in range(length)] for _ in range(length)] for _ in range(length)]
    
    dfs(0,0,0,[0,0])
    print(-1)