import sys 
input = sys.stdin.readline

if __name__ == '__main__':
    B, N, M = list(map(int,input().split()))
    items = dict()
    result = 'acceptable'
    
    for i in range(N):
        i, p = list(input().split())
        items[i] = int(p)
    
    for j in range(M):
        it = input().split()
        if B - items[it[0]] >= 0:
            B -= items[it[0]]
        else:
            result = 'unacceptable'
    
    print(result)
        
    