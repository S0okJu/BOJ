import sys 
input = sys.stdin.readline

def solution(L, K, C, cutting):
    # 조각 구하기 
    pos = [0, *sorted(cutting), L]
    pieces = [pos[i + 1] - pos[i] for i in range(K + 1)]
    longest = max(pieces)
    
    def cut(limit):
        # 조건에 해당되 지않은 경우 
        if longest > limit:
            return 10001, 0
        
        curr_sum = 0
        cuts_used = 0 
        
        # 뒤에서부터 잘라야 가장 처음의 자른 위치를 파악할 수 있음 
        for piece in pieces[::-1]:
            # ?? 
            curr_sum += piece
            if curr_sum > limit:
                cuts_used += 1
                curr_sum = piece
        
        # 컷팅 횟수가 동일할 경우 첫 자른 위치 
        # 남은 조각(curr_sum)
        front_piece = curr_sum if cuts_used == C else pieces[0]
        
        return cuts_used ,front_piece
                
    
    # 자를 수 있는 길이 기준으로 이분 탐색 
    start, end = 0, L
    
    answer_length = 0
    answer_front = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        # 해당 길이의 컷팅 수, 자르는 위치
        cut_cnt, cut_front = cut(mid)
        
        # 현재 값으로도 자를 수 있음
        # 그러나 최소한의 mid 값을 구하는 것이므로 end 조정 
        if cut_cnt <= C:
            answer_length = mid
            answer_front = cut_front
            end = mid -1
        else:
            start = mid + 1
    
    return answer_length, answer_front
    

if __name__ == '__main__':
    L, K, C = map(int, input().split())
    cutting = list(map(int, input().split()))
    
    print(*solution(L, K, C, cutting))
