import sys 
input = sys.stdin.readline

def solution(N, K, sources):
    sources.sort()
    count = 0
    base = sources[0]
    for i in range(1, N):
        while base + sources[i] <= K:
            print(f"{base} {sources[i]}")
            base += sources[i]
            count += 1
    return count
        
        
        
if __name__ == '__main__':
    N, K = map(int, input().split())
    sources = list(map(int,input().split()))
    print(solution(N,K,sources))