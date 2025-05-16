import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = input()
    result = 0

    # 자릿수
    n = len(N)-1
    if n == 1:
        print(N)
    else:
        for i in range(1,n):
            result += (9 * (10**(i-1))) * i
        result += (int(N) - (10**(n-1))+1) * n 
        
        print(result)
