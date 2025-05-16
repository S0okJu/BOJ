def solution(k):
    a_cnt = [0] * 46
    b_cnt = [0] * 46

    # init 
    a_cnt[0] = 0
    b_cnt[0] = 1

    # dp 
    for i in range(1,k):
        a_cnt[i] = b_cnt[i-1]
        b_cnt[i] = a_cnt[i-1] + b_cnt[i-1]
    
    print(f"{a_cnt[k-1]} {b_cnt[k-1]}")
if __name__ == '__main__':
    k = int(input()) 
    solution(k)