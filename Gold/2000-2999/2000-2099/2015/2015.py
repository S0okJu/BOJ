import sys
input = sys.stdin.readline

n, k = map(int, input().split())
input_data = list(map(int, input().split()))  

sum_dict = {0: 1}

sum_ = 0
answer = 0

for i in input_data:
    sum_ += i
    
    # 누적합 x - 누적 합 y = k
    # x- k = y 
    # y가 존재한다면 누적합도 반드시 존재한다는 의미
    if sum_ - k in sum_dict.keys():
        answer += sum_dict[sum_ - k]

    sum_dict[sum_] = sum_dict.get(sum_, 0) + 1
    

print(answer)