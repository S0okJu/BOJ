from collections import deque
import sys 
input = sys.stdin.readline

def solution(N:int):
    init_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # 감소하는 수를 저장하는 큐
    # 결과값을 구하는데 사용 
    desc = []
    desc.extend(init_nums)
    
    # 작업을 수행할때 사용하는 큐 
    work_q = deque(init_nums)
    
    # 1023개만 N을 받을 수 있음
    if N > 1023:
        return -1
    
    while work_q:

        curr = work_q.popleft()
        
        # 일의 자리 숫자를 한차례씩 늘린다. 
        for i in range(0, curr%10):
            desc_num = (curr * 10) + i
            
            desc.append(desc_num)
            work_q.append(desc_num)
    
    #print(desc)
    return desc[N-1]
            
if __name__ == '__main__':
    N = int(input())
    print(solution(N))