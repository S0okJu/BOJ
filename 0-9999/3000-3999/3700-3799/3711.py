from typing import List 
import sys
input = sys.stdin.readline

def find_b(a):
    n = len(a)
    if len(set(a)) != n:
        return None 
    b = n
    while True:
        # 니머지를 구해서 나머지가 서로 unique 한 경우를 찾는다. 
        mods = set([x % b for x in a])
        if len(mods) == n:
            return b  
        b += 1

def solution(G:int, students:List[int]) -> int :
    if G == 1:
        return 1
    return find_b(students)
    
    
if __name__ =='__main__':
    N = int(input().strip())
    
    for i in range(N):
        G = int(input().strip())
        students = [int(input()) for _ in range(G)]

        print(solution(G=G, students=students))
        
        