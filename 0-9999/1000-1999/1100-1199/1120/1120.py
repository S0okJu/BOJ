import sys 
input = sys.stdin.readline

def get_same_len_result(A,B, str_len):
    result = 0 
    for i in range(str_len):
        if A[i] != B[i]:
            result +=1
    
    return result

def get_other_len_result(A,B,A_len, B_len):
    result = 51
    # A길이는 B보다 무조건 작거나 같다.
    for first in range(B_len - A_len+1):
        cnt = 0
        # A 기준으로 탐색
        for a_idx in range(A_len):
            if A[a_idx] != B[a_idx + first]:
                cnt += 1
        
        # print(cnt)
        result = min(result,cnt)
    
    return result
    
            
def solution(A,B):
    # 길이 구하기 
    a_len = len(A)
    b_len = len(B)
    result = 0
    
    # 길이가 같다면 그대로 비교
    if a_len == b_len:
        result = get_same_len_result(A,B, a_len)
    else: # 길이가 같지 않다면 차이가 최소인 것을 찾는다. 
        result = get_other_len_result(A,B,a_len,b_len)
    
    return result
        
    
if __name__ == '__main__':
    A, B = input().split()
    
    print(solution(A,B))
    
    