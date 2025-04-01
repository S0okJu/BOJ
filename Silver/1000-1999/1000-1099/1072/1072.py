import sys 
input = sys.stdin.readline

def solution(X,Y):
    z = (Y * 100) // X
    start, end = 0, 1_000_000_000
    
    result = 0
    while start <= end:
        mid = (start + end)//2
        curr_z = ((Y+mid)*100)//(X+mid)
        # print(curr_z)
        
        if z < curr_z:
            end = mid -1 
            result = mid
        else:
            start = mid + 1
        
    if result == 0:
        return -1

    return result 
        
        
if __name__ == '__main__':
    X, Y = map(int,input().split())
    print(solution(X,Y))