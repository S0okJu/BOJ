if __name__ == '__main__':
    T = int(input())
    
    for i in range(T):
        str_inp = input()
        result = str_inp.split()
        
        words = str_inp.split()
        print(" ".join([word[::-1] for word in words]))
    