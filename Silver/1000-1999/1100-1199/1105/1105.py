import sys 
input = sys.stdin.readline

def solution(L,R):
    str_l = str(L)
    str_r = str(R)
    result = 0 
    
    # 자릿수가 다르면 무조건 0
    if len(str_l) != len(str_r):
        return 0
    
    # 자릿수가 같으면
    for i in range(len(str_l)):
        if str_l[i] != str_r[i]:
            break
        else:
            if str_l[i] =='8':
                result +=1
    
    return result
        
if __name__ == '__main__':
    L, R = map(int,input().split())
    
    print(solution(L,R))