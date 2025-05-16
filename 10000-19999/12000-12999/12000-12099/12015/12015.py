import sys 
input = sys.stdin.readline

def solution(N, A):
    
    m = [0]
    
    for a in A:
        if m[-1] < a:
            m.append(a)
        else:
            # 바로 없을 경우에는 이분 탐색을 통해 숫자를 찾음 O(logn)
            start = 0 
            end = len(m)
            
            while start < end:
                mid = (start + end) //2 
                
                if m[mid] < a:
                    start = mid + 1
                else:
                    # a에 들어갈 인덱스 
                    # 현재 값(a) 보다 클 경우
                    end = mid 
            
            m[end] = a

    return len(m) - 1
if __name__ == '__main__':
    N = int(input())
    A = list(map(int,input().split()))

    print(solution(N,A))
    