import sys 
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    N = []
    for i in range(T):
        n = int(input())
        if n % 2 == 0:
            print(2**(n//2))
        else:
            print(0)
    