import sys
input = sys.stdin.readline

WOLF = 'W'
SHEEP = 'S'
FENCE = 'D'

DIRETIONS = [(-1,0), (0, -1), (1,0), (0,1)]

def is_possible(R, C, fields):

    for r in range(R):
        for c in range(C):
            if fields[r][c] == WOLF:
                for x, y in DIRETIONS:
                    dx, dy = r + x, c + y
                    
                    if 0 <= dx < R and 0<=dy < C:
                        if fields[dx][dy] == SHEEP:
                            return False
    
    return True 
    
if __name__ == '__main__':
    R, C = map(int,input().split())
    
    fields = []
    
    for r in range(R):
        line = input().rstrip()
        fields.append(line)
        
    if not is_possible(R,C,fields):
        print(0)
    else:
        print(1)
        for r in range(R):
            print(fields[r].replace('.','D'))
