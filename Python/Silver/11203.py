def solution():
    
    inputs = input().split()

    h = int(inputs[0])

    # Check if there is a second value for cmd, otherwise assign it an empty string
    cmd = inputs[1] if len(inputs) > 1 else ""
    
    node = 0
    for k in range(h+1):
        node += (2**k)
        
    if cmd == "":
        # print("empty")
        return node 
    
    curr = 1
    node -=curr
    is_right = False
    if cmd[0] == 'R':
        is_right = True
        curr +=1
        node -= 1
    #print(node)
    
    is_minus = False
    for i in range(1, len(cmd)):
        if is_right == True:
            is_minus = True
        if cmd[i] == 'L':
            curr = (2 * curr)
            is_right = False
        else:
            curr = ((2 * curr) + 1)
            is_right = True
        
        if is_minus == True:
            curr -= 1
            
        node -= curr
        
        # print(f"{cmd[i]} {curr} ,{node}")
        is_minus = False
    return node 

if __name__ == '__main__':
    n = solution()
    print(n)
        