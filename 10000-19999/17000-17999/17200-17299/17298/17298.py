import sys 
input = sys.stdin.readline

def timeout_error(N, A):
    stack = []
    stack.append((0,A[0]))
    start = 0 
    
    result = []
    # 전체 순회 
    for i in range(1, N):
        idx, t = stack.pop()
        # 가장 왼쪽에 있는 큰 수 구하기 
        v = 0
        for j in range(idx, N):
            if t < A[j]:
                v = A[j]
                break
        result.append(v if v else -1)
        stack.append((i,A[i]))
    
    result.append(-1)

    return result

def solution(N,A):
    # 인덱스를 기준으로 스택 저장 
    stack = []
    result = [-1] * N
    
    for i in range(N):
        while stack and A[stack[-1]] < A[i]:
            result[stack.pop()] = A[i]
        stack.append(i)
    
    return result
    
if __name__ == '__main__':
    N = int(input())
    A = list(map(int,input().split()))


    print(*solution(N, A))
    