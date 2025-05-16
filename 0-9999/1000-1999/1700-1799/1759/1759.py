import sys 
input = sys.stdin.readline
"""
조건
1. 문자열이 증가하는 순서대로 배치
2. 한 개이상의 모음, 두 개 이상 자음은 무조건 포함되어야 함
"""

VOWELS = {'a', 'e', 'i', 'o', 'u'}
def solution(L, C, lst):
    result = []
    words = []
    visited = [False] * C
    lst.sort()
    
    def backtracking(words):
        if len(words) == L:
            vowel_cnt = sum(1 for word in words if word in VOWELS)    
            if vowel_cnt >= 1 and L-vowel_cnt >= 2:
                result.append(''.join(words))
                return 
        
        before = words[-1] if len(words) > 0 else ''
            
        for i in range(C):
            if not visited[i] and before < lst[i]:
                visited[i] = True
                words.append(lst[i])
                
                backtracking(words)
                
                visited[i] = False
                words.pop()
        
    backtracking(words)
    return result
    

if __name__ == '__main__':
    # Input 
    L, C = map(int,input().split())
    str_lst = list(input().split())
    
    for r in solution(L, C, str_lst):
        print(r)
    
