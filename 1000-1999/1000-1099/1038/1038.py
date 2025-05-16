from collections import deque
import sys
input = sys.stdin.readline

def solution(N: int) -> int:
    if N == 0:
        return 0
    
    # 감소하는 수는 최대 1023개(0~9876543210)
    if N > 1022:  
        return -1

    q = deque()

    # 1자리 수부터 시작 (0~9)
    for i in range(10):
        q.append(i)

    # -1부터 가능하므로
    count = -1 
    
    while q:
        num = q.popleft()
        count +=1
        
        if count == N:
            return num

        last_num = num % 10
        for next_num in range(0, last_num):
            new = (num * 10) + next_num
            q.append(new)
            
if __name__ == '__main__':
    N = int(input())
    print(solution(N))
