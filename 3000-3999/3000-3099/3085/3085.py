import sys 
input = sys.stdin.readline

def solution(N, game):
    dx = [1,0]
    dy = [0,1]
    max_cnt = 0
    
    for x in range(N):
        for y in range(N):
            for d in range(2):
                next_x = x + dx[d]
                next_y = y + dy[d]
                
                # 범위에 벗어난다면 
                if not((0 <= next_x < N) and (0 <= next_y < N)):
                    continue
                
                # 겹친다면 
                if game[x][y] == game[next_x][next_y]:
                    continue
                
                # 겹치지 않는다면..
                game[x][y], game[next_x][next_y] = game[next_x][next_y], game[x][y]
                
                for i in range(N):
                    cnt = 1
                    for j in range(N-1):
                        if game[i][j] == game[i][j+1]:
                            cnt += 1
                            max_cnt = max(cnt, max_cnt)
                        else:
                            cnt = 1
                # print(f"x {max_cnt}")
                for i in range(N):
                    cnt = 1
                    for j in range(N-1):
                        if game[j][i] == game[j+1][i]:
                            cnt += 1
                            max_cnt = max(cnt, max_cnt)
                        else:
                            cnt = 1   
                
                # print(f"y {max_cnt}")     
                # 원상복구   
                game[x][y], game[next_x][next_y] = game[next_x][next_y], game[x][y]
    
    return max_cnt
if __name__ == '__main__':
    N = int(input())
    game = [list(input()) for _ in range(N)]
    
    result = solution(N, game)
    print(result)
