import sys 
input = sys.stdin.readline

def solution(dwarves):
    dwarves.sort()
    result = list()
    
    def comb(current, start):
        if len(current) == 7 and sum(current) == 100:
            result.append(current[:])
            return 
        
        for d in range(start, len(dwarves)):
            current.append(dwarves[d])
            comb(current, d + 1)
            current.pop()
    
    comb(result,0)
    return result
            

if __name__ == '__main__':
    
    dwarves = list()
    for i in range(9):
        n = int(input())
        dwarves.append(n)
    
    real = solution(dwarves)
    
    for r in real:
        print(r)