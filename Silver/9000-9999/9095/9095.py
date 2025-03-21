
def solution(n):
    if n == 1:
        return 1 
    elif n == 2:
        return 2
    elif n == 3:
        # 1 + 2, 2 + 1, 3, 1 + 1 + 1 
        return 4 
    else:
        return solution(n-1) + solution(n-2) + solution(n-3)
     

if __name__ == '__main__':
    T = int(input())
    
    for i in range(T):
        n = int(input())
        print(solution(n))
    