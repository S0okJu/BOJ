def sort(num_list):
    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

if __name__ == '__main__':
    nums = input().split() 
    num_list = [int(x) for x in nums] 
    sort(num_list)
    print(num_list[1])  