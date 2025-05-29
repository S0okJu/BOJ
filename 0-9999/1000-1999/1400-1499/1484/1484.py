import sys
input = sys.stdin.readline

def solution(G: int):
    result = []
    left, right = 1, 2 
    while left < right:
        diff = right * right - left * left
        if diff == G:
            result.append(right)
            right += 1
        elif diff < G:
            right += 1
        else:
            left += 1
    return result

if __name__ == '__main__':
    G = int(input())
    result = solution(G)
    if result:
        print('\n'.join(map(str, result)))
    else:
        print(-1)
