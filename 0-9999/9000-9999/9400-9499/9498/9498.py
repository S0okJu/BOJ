if __name__ == '__main__':
    score = int(input())
    
    result = ''
    if 90 <= score <= 100:
        result = 'A'
    elif 80 <= score < 90:
        result = 'B'
    elif 70 <= score < 80:
        result = 'C'
    elif 60 <= score < 70:
        result = 'D'
    else:
        result = 'F'
    
    print(result)
    