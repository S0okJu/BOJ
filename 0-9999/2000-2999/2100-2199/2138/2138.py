import sys 
input = sys.stdin.readline

def solution(N, status, wanted):
    # 부분 최적해를 구한다 -> 그리디 
    changed = status[:]
    cnt = 0 
    for i in range(1, N):
       # 이전 전구의 값이 다르면
       if changed[i-1] != wanted[i-1]: 
            cnt +=1
            # 주변 전구 변경
            for j in range(i-1, i+2):
                if j < N:
                    changed[j] = 1-changed[j]
    if changed == wanted:
        return cnt 
    else:
        return 1e9
            
       
    
if __name__ == '__main__':
    N = int(input())
    status = list(map(int, input().strip()))
    wanted = list(map(int, input().strip()))
    
    first_off = solution(N, status, wanted)
    
    # 첫번째 전구를 누르는 경우
    status[0] = 1- status[0]
    status[1] = 1- status[1]
    
    first_on = solution(N, status, wanted) + 1
    
    result = min(first_off, first_on)
    if result != 1e9:
        print(result)
    else:
        print(-1)
        
    
    
