import sys 
inpupt = sys.stdin.readline

def is_match(a: str, b: str) -> bool:
    """
    Only a=b=2 does not matched. 
    """
    return not (a == '2' and b == '2')

def solution(A: str, B: str) -> int:
    n, m = len(A), len(B)
    result = n + m

    # gear2를 기준으로 left -> right 이동함 
    for offset in range(-m, n+1):
        ok = True 
        for i in range(m):  
            j = i + offset 
            if 0 <= j < m:
                if not is_match(a=A[j],b=B[i]):
                    ok = False 
        
        if ok:
            left = min(left, offset)
            right = max(right, offset + m)
            result = max(result, right-left)
    
    return result
            

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    A = input().strip()
    B = input().strip()
    print(solution(A, B))
