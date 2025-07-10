def solve():
    N = int(input())
    
    commands = []
    for _ in range(N):
        cmd, tgt, time  = input().strip().split()
        commands.append((int(time), cmd, tgt))
    
    executed = [True] * len(commands)
    
    for i in range(len(commands) - 1, -1, -1):
        time, cmd_type, param = commands[i]
        
        if not executed[i]:
            continue
            
        if cmd_type == 'undo':
            for j in range(i):
                target_time = commands[j][0]
                if time - int(param) <= target_time < time:
                    executed[j] = not executed[j]
    
    result = []
    for i in range(len(commands)):
        if commands[i][1] == 'type' and executed[i]:
            result.append(commands[i][2])
    
    return ''.join(result)

if __name__ == '__main__':
    print(solve())