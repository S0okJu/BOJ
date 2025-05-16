import sys

input = sys.stdin.readline

def solution(N, K):
    digit_length = 1
    count = 9
    start = 1

    # 현재 위치 찾기
    while K > digit_length * count:
        K -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10

    # 실제 숫자 찾기
    num = start + (K - 1) // digit_length

    # 숫자 N을 초과하는 경우
    if num > N:
        print(-1)
    else:
        print(str(num)[(K - 1) % digit_length])

if __name__ == '__main__':
    N, K = map(int, input().split())
    solution(N, K)
