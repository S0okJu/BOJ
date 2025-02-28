import sys
input = sys.stdin.readline

def solution():
    n,m = map(int, input().split())
    
    nums = sorted(list(set(list(map(int,input().split())))))
    answers = []
    
    def backtracking(arr):
        if len(arr) == m:
            answers.append(arr[:])
            return
    
        for i in range(len(nums)):
            if not arr or arr[-1] <= nums[i]:
                arr.append(nums[i])
                backtracking(arr)
                arr.pop()
                
    backtracking([])
    
    for answer in answers:
        print(*answer)

if __name__ == '__main__':
    solution()