import sys 
input = sys.stdin.readline

def can_see(heights, from_idx, to_idx):
    """
    from_idx 빌딩에서 to_idx 빌딩이 보이는지 확인
    두 지붕을 잇는 직선이 중간 빌딩들을 지나거나 접하지 않으면 보임
    """
    if from_idx == to_idx:
        return False
    
    # 시작점과 끝점의 좌표
    x1, y1 = from_idx, heights[from_idx]
    x2, y2 = to_idx, heights[to_idx]
    
    # 구간 정의 (from_idx와 to_idx 사이)
    start = min(from_idx, to_idx)
    end = max(from_idx, to_idx)
    
    # 중간에 있는 모든 빌딩 확인
    for i in range(start + 1, end):
        # x = i일 때의 직선 높이 계산
        line_height = y1 + (y2 - y1) * (i - x1) / (x2 - x1)
        
        # 중간 빌딩이 직선보다 높거나 같으면 가려짐
        if heights[i] >= line_height:
            return False
    
    return True
def solution(N, heights):
    max_visible = 0
    
    for i in range(N):
        visible_count = 0
        
        # 왼쪽 빌딩들 확인
        for j in range(i):
            if can_see(heights, i, j):
                visible_count += 1
        
        # 오른쪽 빌딩들 확인
        for j in range(i + 1, N):
            if can_see(heights, i, j):
                visible_count += 1
        
        max_visible = max(max_visible, visible_count)
    
    return max_visible

if __name__ == '__main__':
    N = int(input())
    heights = list(map(int,input().split()))
    
    print(solution(N=N,heights=heights))
