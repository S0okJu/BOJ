import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count_map = defaultdict(int)
count_map[0] = 1  

count = 0
diff_sum = 0  

for i in range(N):
    # D[i] = (A의 누적합) - (B의 누적합)
    diff_sum += A[i] - B[i]  
    
    # 누적합이 같으면 무조건 diff_sum은 0이 나옴 
    count += count_map[diff_sum]
    count_map[diff_sum] += 1


print(count)