
def solution():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = a + b 
    c.sort()
    print(' '.join(map(str,c)))

if __name__ == '__main__':
    solution()
