def solution(inp):

    idx = int(inp)+1
    result = -1
    while idx <= 9999:
        front = int(idx / 100)
        end = int(idx % 100)
        # print(f"{(front + end) }")
        if (front + end)**2 == idx:
            result = idx 
            break 
        idx+=1
    
    print(result)
    
if __name__  == '__main__':
    inp = input()
    solution(inp=inp)
    