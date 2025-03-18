def add_digit(digit, num):
    if digit==1:
        decreasing.append(num)
    else:
        # 2이면 뒤의 자리숫에는 0,1 만 사용할 수 있으므로 
        for i in range(num%10):
            add_digit(digit-1,num*10+i)

n = int(input())
decreasing = list()

# 자릿수 
for digit in range(1,11):
    # 뒤에 올 숫자 0 ~ 9
    for num in range(digit-1, 10):
        add_digit(digit,num)
        
if n >= len(decreasing):
    print(-1)
else:
    print(decreasing[n])
        