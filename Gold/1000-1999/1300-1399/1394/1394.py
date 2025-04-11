from collections import deque

import sys
input = sys.stdin.readline

def memory_out(available:str, target:str) -> int:
    """
    deque에서 데이터를 과도하게 삽입하여 메모리 초과(OOM)이 발생함 
    """
    str_lst = [ch for ch in available]
    
    work_deque = deque(str_lst)
    cnt = 0
    while work_deque:
        curr_str = work_deque.popleft()
        # print(curr_str)
        cnt = (cnt+1) % 900528
        
        if curr_str == target:
            break 
        else:
            for ch in str_lst:
                work_deque.append(curr_str+ch)
    
    return cnt

def timeout(available: str, target: str) -> int:
    """
    지수 연산으로 인해 시간 초과가 발생함 
    """
    chars = [ch for ch in available]
    radix = len(chars)
    char_to_digit = {ch: i for i, ch in enumerate(chars)}

    count = 0
    for l in range(1, len(target)):
        count += radix ** l  # 길이 l인 문자열 개수 누적(타임아웃 원인)

    for i, ch in enumerate(target):
        digit = char_to_digit[ch]
        remaining = len(target) - i - 1
        count += digit * (radix ** remaining)

    return (count + 1) % 900528  # 인덱스 1-based로 맞춤

def solution(available: str, target: str) -> int:
    MOD = 900528
    char_to_idx = {ch:i+1 for i,ch in enumerate(available)}
    
    result = 0
    base = len(available)
    
    for ch in target:
        result = (result * base + char_to_idx[ch])%MOD
    
    return result
    

if __name__ == '__main__':
    available = input().rstrip()
    target = input().rstrip()
    
    print(solution(available, target))