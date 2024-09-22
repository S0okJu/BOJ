if __name__ == '__main__':
    n = int(input())
    students = input().split()
    
    students_dict = dict()
    for i in range(n):
        students_dict[students[i]] = 0 
    
    for j in range(n):
        pop_students = list()
        pop_students = input().split()
        
        for idx in range(len(pop_students)):
            students_dict[pop_students[idx]] += 1
    
    students_dict = sorted(students_dict.items(), key=lambda x:x[1],reverse=True)
    for k, v in students_dict:
        print(f"{k} {v}")
    