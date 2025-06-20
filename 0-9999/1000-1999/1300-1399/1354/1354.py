import sys 
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def solution(N, P, Q, X, Y):
    memo = {0: 1}
    stack = deque([N])

    while stack:
        i = stack[-1]  

        if i in memo:
            stack.pop()
            continue

        a = i // P - X
        b = i // Q - Y

        if a < 0:
            memo[a] = 1
        if b < 0:
            memo[b] = 1

        if a not in memo:
            stack.append(a)
        elif b not in memo:
            stack.append(b)
        else:
            memo[i] = memo[a] + memo[b]
            stack.pop()

    return memo[N]

if __name__ == '__main__':
    N, P, Q, X, Y = map(int,input().split())  
    print(solution(N,P,Q,X,Y))
    
