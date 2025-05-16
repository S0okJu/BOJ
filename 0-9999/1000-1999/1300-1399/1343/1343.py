def solution(board):
    result = ''
    
    blocks = []
    start = 0
    for i in range(1, len(board)):
        if board[i] != board[i-1]:
            blocks.append(board[start:i])
            start = i
    blocks.append(board[start:])  # 마지막도 포함
    # print(blocks)
    # X 채우기

    for x_idx in range(len(blocks)):
        # 2의 배수가 아니면 바꿀 수 없음
        if blocks[x_idx][0] == '.':
            result += blocks[x_idx]
            continue
        
        x_len = len(blocks[x_idx])
        if x_len % 2 != 0:
            return -1 
        
        a_cnt = x_len // 4
        b_cnt = (x_len % 4) // 2
        
        converted_x =''
        if a_cnt > 0:
            converted_x += 'AAAA' * a_cnt
        
        if b_cnt >0:
            converted_x += 'BB' * b_cnt
        
        result += converted_x
    

    return result
      
        
if __name__ == '__main__':
    
    inp = input()
    print(solution(inp))
    