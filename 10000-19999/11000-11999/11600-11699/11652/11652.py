from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    
    num_dict = defaultdict(int)
    nums = []
    for i in range(N):
        n = int(input())
        num_dict[n] += 1
        
    max_value = max(num_dict.values())
    max_keys = [k for k,v in num_dict.items() if v == max_value]
    
    print(min(max_keys))
    