import sys 
input =  sys.stdin.readline

def solution(N, cands):
    
    # [(1, 4), (2, 5), (3, 6), (4, 2), (5, 7), (6, 1), (7, 3)]
    cands.sort()
    
    # 1차 1등은 우선 선별함 
    result = 1
    
    # 2차를 기준으로 합격자 선발 
    # 1차에서 1등한 합격자의 2차 순위를 기반으로 합격자 선별 
    # 단 1등 1차보다 2차 순위가 높은 후보자 내에서도 합격자를 선발해야 하므로 
    # 2차 등수의 범위를 지속적으로 조정
    min_second = cands[0][1]
    
    for i in range(1,N):
        if cands[i][1] < min_second:
            result +=1
            min_second = cands[i][1]
    
    return result
            
    
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        cands = []
        for i in range(N):
            first, second = map(int,input().split())
            cands.append((first,second))
        
        print(solution(N, cands))
