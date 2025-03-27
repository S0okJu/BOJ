import sys 
input = sys.stdin.readline

def solution(N, M, A, B):
    # 처음부터 완전히 같은 경우 
    if A== B:
        return 0
    
    result = 0 
    # 시작 범위 정하기  
    for i in range(N-2):
        for j in range(M-2):
            # 처음 숫자가 같지 않으면 스왑 조건에 해당 
            # 3 x 3 씩 변경 
            if A[i][j] != B[i][j]:
                result += 1
                for ax in range(i, i+3):
                    for by in range(j, j+3):
                        A[ax][by] ^= 1

            # 같으면 결과 반환 
            if A == B:
                return result
    
    # 나머지는 모두 오류 반환
    # N, M 길이가 3보다 작다면 무조건 기존의 A로 유지됨(스왑 발생하지 않음)              
    return -1 
                
if __name__ == '__main__':
    N, M = map(int,input().split())
    
    A = [list(map(int, input().strip())) for _ in range(N)]
    B = [list(map(int, input().strip())) for _ in range(N)]
    
    print(solution(N, M, A,B))