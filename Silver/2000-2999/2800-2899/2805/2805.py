import sys 
input = sys.stdin.readline

def solution(N,M,trees):
    trees.sort()
    start = 0
    result = 0
    end = trees[-1]
    
    while start <= end:
        remainder = 0 
        mid = (start + end) // 2
            
        # 나무 자르기
        for tree in trees:
            # 나무가 절단기보다 크기가 커야함
            if tree >= mid:
                remainder += (tree-mid)
        
        
        # 남은 것이 클 경우 절단기 크기를 더 키워야 함
        if remainder >= M:
            result = mid 
            start = mid + 1
        else:
            end = mid -1
    
    return result
if __name__ == '__main__':
    N, M = map(int,input().split())
    trees = list(map(int,input().split()))
    
    print(solution(N,M,trees))