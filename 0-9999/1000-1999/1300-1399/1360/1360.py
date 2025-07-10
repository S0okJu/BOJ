def solve():
    N = int(input())
    
    # 명령어 저장: (시간, 명령어타입, 내용)
    commands = []
    for _ in range(N):
        cmd, tgt, time  = input().strip().split()
        commands.append((int(time), cmd, tgt))
    
    # 역순으로 각 명령어의 실행 여부를 계산
    executed = [True] * len(commands)
    
    # 뒤에서부터 앞으로 처리
    for i in range(len(commands) - 1, -1, -1):
        time, cmd_type, param = commands[i]
        
        if not executed[i]:
            continue
            
        if cmd_type == 'undo':
            for j in range(i):
                target_time = commands[j][0]
                if time - int(param) <= target_time < time:
                    executed[j] = not executed[j]
    
    # 최종 결과 구성
    result = []
    for i in range(len(commands)):
        if commands[i][1] == 'type' and executed[i]:
            result.append(commands[i][2])
    
    return ''.join(result)

if __name__ == '__main__':
    print(solve())