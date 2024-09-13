
def counter(n,candidates):
    if n == 1:
        return 0
    
    dasom = candidates[0]
    sorted_candidates = sorted(candidates[1:])
    cnt = 0
    equal_num_cnt = 0
    
    for i in range(len(sorted_candidates)):
        if sorted_candidates[i] > dasom:
            while True:
                if sorted_candidates[i] <= dasom:
                    break
                else:
                    sorted_candidates[i] = sorted_candidates[i] - 1
                    dasom = dasom + 1
                    cnt = cnt+1
    
        elif sorted_candidates[i] == dasom:
            equal_num_cnt
    
    if equal_num_cnt == len(sorted_candidates):
        return 1
            
    return cnt 


if __name__ == "__main__":
    n = input()
    candidates = list()
    for i in range(int(n)):
        inp = input()
        candidates.append(int(inp))
    
    cnt = counter(int(n), candidates)
    print(cnt)