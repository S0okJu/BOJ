def solution(notes: list) -> int:
    stack = []
    for num in notes:
        #  print(notes)
        if num != 0:
            stack.append(num)
        else:
            if len(stack) > 0:
                stack.pop()
    
    return sum(stack)

if __name__ == '__main__':
    K = int(input())
    notes = list()
    
    for i in range(K):
        notes.append(int(input()))
    
    print(solution(notes))