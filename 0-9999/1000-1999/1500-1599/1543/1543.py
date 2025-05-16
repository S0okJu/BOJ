
def solution(S:str, target:str) -> int:

    s_len = len(S)
    target_len = len(target)
    idx = 0
    cnt = 0
    while idx <= s_len -target_len:
        end = idx + target_len
        if S[idx:end] == target:
            idx += target_len
            cnt +=1
        else:
            idx += 1
        
    return cnt 
                
if __name__ == '__main__':
    S = input()
    target = input()
    print(solution(S, target))