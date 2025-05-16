board = str(input())
board+='.'
cnt = 0
ans = 0

for i in range(len(board)):
    if board[i]=='X':
        cnt= cnt+1
    if board[i] =='.':
        if cnt%2 ==0:
            continue
        else:
            ans = -1
            break


if ans ==0:
    board = board.replace('XXXX','AAAA')
    board = board.replace('XX','BB')
    print(board[:-1])
else:
    print(ans)


