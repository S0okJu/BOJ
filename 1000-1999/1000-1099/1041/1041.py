import sys
input = sys.stdin.readline

def solution(N,dice):
    if N == 1:
        return sum(dice) - max(dice)

    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] 
    
    # 한 면만 보일때
    one = min(dice)
    
    # 두 면만 보일때 
    side_2 = [(a, b), (a, c), (a, d), (a, e), (b, d), (e, d), (e, c), (c, b), (d, f), (b, f), (c, f), (e, f)]
    two = sum(side_2[0])
    for i, j in side_2:
        two = min(two, i + j)
    
    # 세 면만 보일때
    side_3 = [(a, b, c), (a, c, e), (a, d, b), (a, e, d), (d, f, b), (b, f, c), (c, f, e), (e, f, d)]
    three = sum(side_3[0])
    for i,j,k in side_3:
        three = min(three, i+j+k)
        
    ans = 0
    ans += (4 * (N - 1) * (N - 2) + (N - 2) * (N - 2)) * one
    ans += ((N - 1) * 4 + (N - 2) * 4) * two
    ans += 4 * three
    return ans


if __name__ == '__main__':
    N = int(input())
    dice = list(map(int,input().split()))
    print(solution(N,dice))