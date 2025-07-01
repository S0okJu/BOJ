from sys import stdin

input = stdin.readline

def solution(n, solvent):
    ans = float("INF")
    left = 0 
    right = 0
    
    for i in range(n-1):
        current = solvent[i]
        start = i + 1
        end = n - 1
        
        while start <= end:
            mid = (start + end )// 2
            tmp = current + solvent[mid]
            
            if abs(tmp) < ans:
                ans = abs(tmp)
                left = i
                right = mid 
                
                if tmp == 0:
                    break 
            
            if tmp < 0:
                start = mid + 1
            else:
                end = mid - 1

            # print(f"{left} {right}")
    print(f"{solvent[left]} {solvent[right]}")
                

if __name__ == '__main__':
    n = int(input())
    solvent = sorted(list(map(int,input().split())))
    
    solution(n, solvent)