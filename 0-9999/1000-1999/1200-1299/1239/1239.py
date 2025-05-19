import sys 
from itertools import permutations
input = sys.stdin.readline


class Chart:
    def __init__(self, N:int, nums_arr:list):
        self._N = N
        self._nums_arr = nums_arr
        self._prefix_sum = list()
    
    def _prepare_prefix_sum(self, perm ):
        self._prefix_sum = []
        curr_sum = 0
        for num in perm:
            curr_sum += num 
            self._prefix_sum.append(curr_sum)
            
    def _count_central_line(self, perm):
        self._prepare_prefix_sum(perm)
        cnt = 0
        sum_len = len(self._prefix_sum)
        for i in range(sum_len-1):
            for j in range(i+1, sum_len):
                if self._prefix_sum[j] - self._prefix_sum[i] == 50:
                    cnt +=1
        
        return cnt
    
    def find_central_line(self):
        max_lines = 0
        for perm in permutations(self._nums_arr):
            max_lines = max(max_lines, self._count_central_line(perm))
        
        return max_lines


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int,input().split()))

    if max(numbers) > 50:
        print(0)
    else:
        chart = Chart(N=N, nums_arr=numbers)
        print(chart.find_central_line())