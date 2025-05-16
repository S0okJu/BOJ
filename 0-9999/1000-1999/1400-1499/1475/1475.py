from collections import defaultdict
import math 
import sys 
input = sys.stdin.readline

def solution(N:str) -> int:
    num_dict = defaultdict(int)
    
    for n in N:
        num_dict[n] += 1
    
    six_nine_count = num_dict['6'] + num_dict['9']
    six_nine_set_count = math.ceil(six_nine_count / 2)  
        
    excluded = {'6','9'}
    filtered = [v for k, v in num_dict.items() if k not in excluded]
    other_max = max(filtered) if filtered else 0
    result = max(other_max, six_nine_set_count)
    
    return result
            

if __name__ == '__main__':
    N = input().rstrip()
    print(solution(N))