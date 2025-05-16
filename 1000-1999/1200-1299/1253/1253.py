from typing import List
import sys 
input = sys.stdin.readline

# 중복이 많아서 비효율적
# 1 + 2, 2 + 1 모두 같지만 다른 연산으로 처리됨 
def Failed(N:int, numbers:List) -> int:
    sums_set = set()
    graph = []
    visited = [False for _ in range(N)]
    def backtracking(graph: List):
        if len(graph) == 2:
            sums_set.add(sum(graph))
            return 
        
        for n in range(N):
            if not visited[n]:
                visited[n] = True 
                graph.append(numbers[n])

                backtracking(graph)

                graph.pop()
                visited[n] = False
    
    backtracking(graph)
    
    result = len(set(numbers) & sums_set)
    return result

def solution(N: int, numbers: List[int]) -> int:
    numbers.sort()
    count = 0

    for target in numbers:
        start, end = 0, N-1
        while start < end:
            # 포인터가 정확하게 target과 동일한 경우
            if target == numbers[start]:
                start +=1
                continue
            elif target == numbers[end]:
                end -=1
                continue
           
            # 겹치지 않는 경우
            sums = numbers[start] + numbers[end]
            if sums == target:
                count += 1
                break 
            elif sums > target:
                end-=1
            elif sums < target:
                start+=1

        
    return count

    # 횟수 세기     
if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int,input().split()))
    
    print(solution(N, numbers))