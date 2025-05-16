# 시간 복잡도 : O(mx-mn) 
def solution():
    mn, mx = map(int, input().split())
    cnt = mx - mn + 1
    table = [True] * cnt 

    for i in range(2, int(mx**0.5)+1):
        # mn보다 크거나 같으면서 i*i의 배수인 경우를 구하기 
        for j in range((mn//(i*i))*(i*i), mx +1, i*i):
            # j가 mn 이상이면서 아직 확인되지 않은 경우(True)
            if j >= mn and table[j-mn]:
                cnt -=1
                table[j-mn]=False # 제곱수 배수로 표시 

    print(cnt)

if __name__ == '__main__':
    solution()