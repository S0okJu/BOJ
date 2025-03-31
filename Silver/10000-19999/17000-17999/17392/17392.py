import sys 
input = sys.stdin.readline

def solution(N,M,holidays):

    holiday = M - N - sum(holidays)
    result = 0
    for i in range(holiday):
        # 긱 휴일 i를 N+1 구간에서 순서대로 하나씩 배치
        # i // (N+1)는 몇번째 라운드 휴일인지 계산 
        # 배치될 경우 우울함이 증가 
        result += (i//(N+1)+1)**2
    return result

if __name__ == '__main__':
    N, M = map(int,input().split())
    if N == 0:
        holidays = [0]
    else:
        holidays = list(map(int,input().split()))
    print(solution(N,M,holidays))