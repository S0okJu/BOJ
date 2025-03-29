import sys 
input = sys.stdin.readline

def solution(N,D,K,daily):
    stars = [0] * N
    result = 0 
    for i in range(D):
        # 더하기 
        stars = [stars[v]+daily[v] for v in range(N)]
        is_clean = False 
        for star in stars:
            # 임계치보다 크다면 
            if star > K:
                stars = daily[:]
                is_clean = True 
                break
        # print(stars)
        if is_clean:             
            result += 1    
    return result
            

if __name__ == '__main__':
    N, D, K = map(int,input().split())
    daily = list(map(int,input().split()))
    
    print(solution(N,D,K,daily))