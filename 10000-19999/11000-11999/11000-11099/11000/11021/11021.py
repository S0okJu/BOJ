
def solution(idx, A, B):
    print(f"Case #{idx}: {A+B}")

if __name__ == '__main__':
    T = int(input())
    
    for t in range(T):
        A, B = map(int,input().split())
        solution(idx=t+1, A=A, B=B)
        