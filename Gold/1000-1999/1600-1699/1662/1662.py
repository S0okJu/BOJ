def solution(compressed: str) -> int:
    stack = []

    for ch in compressed:
        if ch == ')':
            temp = 0

            # 괄호 안 문자열 길이 계산
            while stack:
                top = stack.pop()
                if top == '(':
                    break
                elif isinstance(top, int):
                    temp += top
                else:
                    temp += 1

            # 괄호 앞에 있는 숫자 확인 (곱셈)
            if stack and stack[-1].isdigit():
                multiplier = int(stack.pop())
                stack.append(temp * multiplier)
            else:
                stack.append(temp)
        else:
            stack.append(ch)

    # 최종 길이 계산
    total_length = 0
    print(stack)
    for item in stack:
        if isinstance(item, int):
            total_length += item
        else:
            total_length += 1

    return total_length

if __name__ == '__main__':
    S = input()
    print(solution(S))
    