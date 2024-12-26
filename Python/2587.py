
def sort(num_list):
    for i in range(len(num_list)-1):
        for j in range(len(num_list)-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]


if __name__ == "__main__":
    num_sum = 0
    num_list = list()
    for i in range(5):
        num = input()
        num_list.append(int(num))
        num_sum = num_sum + int(num)
    
    print(int(num_sum/5))
    
    sort(num_list)
    print(num_list[2])
    
    
        