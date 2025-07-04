import sys 
inpupt = sys.stdin.readline

def is_match(a: str, b: str) -> bool:
    return not (a == '2' and b == '2')

def solution(A: str, B: str) -> int:
    gear1, gear2 = A.strip(), B.strip()
    n, m = len(gear1), len(gear2)
    min_len = n + m

    for offset in range(-m, n+1):
        ok = True
        for i in range(m):
            j = i + offset
            if 0 <= j < n:
                if not is_match(gear1[j], gear2[i]):
                    ok = False
                    break
        if ok:
            left = min(0, offset)
            right = max(n, offset + m)
            min_len = min(min_len, right - left)
    return min_len

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    A = input().strip()
    B = input().strip()
    print(solution(A, B))