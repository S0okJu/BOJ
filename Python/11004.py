
def solution():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[k-1])


if __name__ == '__main__':
    solution()