import sys 
input = sys.stdin.readline

n, k = map(int, input().split())

total = []
cnt = 0 

def backtracking():
    global cnt
    if sum(total) > n:
        return 
    
    if sum(total)==n:
        # k 번째 수 구하기 
        if cnt == (k-1):
            print(*total, sep='+')
            exit()
        else:
            cnt +=1
            return 
    
    # 1, 2, 3 중 하나씩 추가 
    for i in range(1,4):
        total.append(i)
        backtracking()
        total.pop()
        

backtracking()
print(-1)