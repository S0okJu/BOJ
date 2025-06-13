import sys 
input = sys.stdin.readline

def solution(N, height):
    result = [0] * N
    for i in range(N):
        count = 0
        for j in range(N):
            if result[j] == 0:
                if count == height[i]:
                    result[j] = i + 1
                    break
                count += 1
    return result  

if __name__ == '__main__':
    N = int(input())
    height = list(map(int,input().split()))
    
    print(*solution(N,height))