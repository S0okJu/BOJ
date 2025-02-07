import sys

input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))

solutions = sorted(solutions)

left, right = 0 , n-1
minDiff = 2000000000
ans1, ans2 = 0, 0

while left < right:
    total = solutions[left] + solutions[right]
    abs_total = total
    if total < 0:
        abs_total = -abs_total
    
    
    if abs_total < minDiff:
        minDiff = abs_total 
        ans1, ans2 = solutions[left], solutions[right]
    
    if total < 0:
        left = left + 1
    else:
        right = right -1
    
    

print(ans1, ans2)
