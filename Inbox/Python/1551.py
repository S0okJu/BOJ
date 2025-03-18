def calculate(n, k, arr):
    if n == 1:
        return arr
    
    for j in range(k):
        calculated_arr = list()  # Fix the typo "calculated" instead of "caculated"
        for i in range(n-1):
            calculated_arr.append(arr[i+1] - arr[i])
        arr = calculated_arr
        n = n - 1

    return arr  # Return arr instead of the possibly undefined calculated_arr

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split(',')))

    result = calculate(n, k, arr)
    print(','.join(map(str, result)))
