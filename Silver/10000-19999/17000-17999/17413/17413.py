import sys 
input = sys.stdin.readline
if __name__ == '__main__':
    S = input()
    tokens = []
    is_bracket = []
    tmp = ''
    in_bracket = False

    for char in S:
        if char == '<':
            if tmp:
                tokens.append(tmp)
                is_bracket.append(in_bracket)
                tmp = ''
            in_bracket = True
            tmp += char
        elif char == '>':
            tmp += char
            tokens.append(tmp)
            is_bracket.append(in_bracket)
            tmp = ''
            in_bracket = False
        else:
            tmp += char

    if tmp:
        
        is_bracket.append(in_bracket)
        tokens.append(tmp)

    for i in range(len(tokens)):
        if is_bracket[i]:
            print(tokens[i], end='')
        else:
            processing_token =tokens[i].split()
            print(' '.join(word[::-1] for word in processing_token) , end='')
        
            