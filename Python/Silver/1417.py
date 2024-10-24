
def counter(n,candidates):
    cnt = 0
    if n == 1:
        return 0
    
    while candidates.index(max(candidates)) != 0:
        candidates[candidates.index(max(candidates))] -= 1    
        candidates[0] +=1
        cnt +=1
    
    for i in range(1,n):
        if candidates[0] == candidates[i]:
            candidates[0] +=1
            candidates[i] -=1
            cnt +=1
    return cnt 


if __name__ == "__main__":
    n = input()
    candidates = list()
    for i in range(int(n)):
        inp = input()
        candidates.append(int(inp))
    
    cnt = counter(int(n), candidates)
    print(cnt)