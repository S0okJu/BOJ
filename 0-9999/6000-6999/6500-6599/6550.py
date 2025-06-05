
def solution(s, t):
    len_s = len(s)
    len_t = len(t)
    
    if len_s > len_t:
        return 'No'
    
    s_idx = 0
    for t_idx in range(len_t):
        
        if s_idx  < len_s and s[s_idx] == t[t_idx] :
            s_idx += 1
    
    return 'Yes' if s_idx == len_s else 'No'
    
if __name__ == '__main__':
    
    while True:
        try:
            s, t = input().split()
            print(solution(s,t))
        
        except (KeyboardInterrupt, EOFError):
            break
        
        
