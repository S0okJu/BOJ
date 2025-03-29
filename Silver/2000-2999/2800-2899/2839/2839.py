import sys
input = sys.stdin.readline

def solution(N):
    result = 0
    
    # 3, 5 가 섞인 경우 
    # 5를 나눈 나머지 값이 3의 배수일 경우에만 5를 나눈다.
    for i in range(N//5, -1, -1):
        remainer = N -  (5 * i)
        # 완전한 5의 배수일 경우 
        if remainer == 0:
            return i
        
        # 5를 사용하고 남은 숫자가 3의 배수라면 3으로 채운다.
        if remainer%3 == 0:
            return i + (remainer//3)
    
    return -1
  
if __name__ == '__main__':
    N = int(input())
    print(solution(N))