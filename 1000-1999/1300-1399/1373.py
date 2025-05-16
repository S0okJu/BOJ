def solution(bits):
    num_list = list()
    bits_len = len(bits)
    
    rot_cnt = bits_len // 3
    for i in range(rot_cnt):
        rot_idx = bits_len - (int(i) * 3) 
        num_list.append(bits[rot_idx -3:rot_idx])
        
    remain = bits_len % 3 
    if remain != 0:
        zero = ""
        for j in range(3 - remain):
            zero += "0"
        
        num_list.append(zero + bits[:remain])
        
    result = converter(num_list)
    
    return result

def converter(num_list):
    num_sum_list = list()
    for num in num_list:
        num_sum = 0
        num_sum += ( (2 ** 2) * int(num[0])) + ( (2 ** 1) * int(num[1])) + ( (2 ** 0) * int(num[2]))
        num_sum_list.append(num_sum)
    
    return num_sum_list

if __name__ == "__main__":
    bits = input()
    result = solution(bits)
    print(''.join(str(x) for x in reversed(result)))