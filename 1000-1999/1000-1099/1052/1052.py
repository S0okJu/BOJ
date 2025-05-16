import sys 
input = sys.stdin.readline

def solution(N:int, K:int) -> int:
    count = 0
    
    # 1. N의 값의 이진수 1개수가 K보다 넘지 않을때까지 반복해서 물병 개수(N)를 추가한다.
    while bin(N).count('1') > K:
        N+=1 
        # 2. 반복한 횟수를 통해 추가한 물병의 수(count)를 구한다.
        count += 1
    
    return count 


if __name__ == '__main__':
    N, K = map(int,input().split())
    print(solution(N,K))