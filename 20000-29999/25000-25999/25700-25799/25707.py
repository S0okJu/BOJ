if __name__ == '__main__':
    N = int(input())
    beads = list(map(int,input().split()))
    
    beads.sort()
    
    result = 0
    for i in range(1,N):
        result += abs(beads[i] - beads[i-1])
    
    result += abs(beads[N-1] - beads[0]) 
    
    print(result)
        