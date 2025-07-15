import sys 
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    s = [0] * (n + 1)

    # i + 1명까지 고려 
    for i in range(n):
        # 현재 학생부터 시작 
        mx = mn = a[i]
        # j -> i까지 한 조 
        for j in range(i, -1, -1):
            # 조 내 최고점수
            mx = max(mx, a[j])
            # 조 내 최저점수
            mn = min(mn, a[j])
            # i+1으로 한 조인 경우, 0 ~ j 까지 한 조 이면서 j ~ i가 한 조인 경우 
            s[i + 1] = max(s[i + 1], s[j] + mx - mn)

    print(s[n])