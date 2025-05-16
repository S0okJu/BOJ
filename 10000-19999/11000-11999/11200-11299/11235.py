if __name__ == '__main__':
    n = int(input())
    candidates = dict()

    for i in range(n):
       candidate = input()
       
       if candidate in candidates:
           candidates[candidate] += 1
       else:
           candidates[candidate] = 1
    
    
    sorted_candidates = sorted(candidates.items(), key=lambda x:x[1], reverse=True)
    top_list = list()
    max_cnt = sorted_candidates[0][1] 
    for k,v in sorted_candidates:
        
        if v == max_cnt:
            top_list.append(k)
        else:
            break
    
    top_list = sorted(top_list)
    for i in top_list:
        print(i)
