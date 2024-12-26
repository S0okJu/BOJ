if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    result = list()
    for i in range(n):
        result.insert(arr[i], i+1)
    result.reverse()
    
    print(' '.join(map(str, result)))