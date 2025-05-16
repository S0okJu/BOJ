def solution(N:int, K: int, num: list) -> str:
    delK=K

    result = []

    for i in range(N):
        while delK and result:
            if result[-1] < num[i]:
                result.pop()
                delK-=1
            else:
                break
        result.append(num[i])
        print(result)
    # 정해진 숫자만 반환해야 하므로 N-K 수행 
    return ''.join(result[:N-K])

if __name__ == '__main__':
    N, K = map(int, input().split())
    num = list(input())
    print(solution(N,K, num))
