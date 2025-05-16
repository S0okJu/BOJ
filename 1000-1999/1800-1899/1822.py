"""
복잡도 : O(nlogn)
"""


def solution():
    an, bn = map(int,input().split())
    a = set(map(int,input().split()))
    b = set(map(int,input().split()))
    
    result = a - b  # O(n)
    result = sorted(list(result)) # O(nlogn)
    if len(result) == 0:
        print("0")
    else:
        print(len(result))
        print(' '.join(map(str,result))) # O(n)


if __name__ == '__main__':
    solution()
        
