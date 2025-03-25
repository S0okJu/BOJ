import sys
input = sys.stdin.readline

def get_x_at_y(start_x, start_y, target_y, dest_x):
    """
    (start_x, start_y)에서 (dest_x, 0)까지 가는 선분이 target_y(y=y1)을 지나는 지점의 x좌표
    """
    dx = dest_x - start_x
    dy = -start_y  # y=0까지 내려가는 직선의 높이 차이
    if dx == 0:
        return start_x
    slope = dy / dx
    return start_x + (target_y - start_y) / slope

if __name__ == '__main__':
    W, H = map(int, input().split())
    x, y = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    # 골대 높이는 y1 == y2
    # 와니가 x=0으로 찼을 때 궤적이 y=y1에서 도달하는 x좌표
    left = get_x_at_y(x, y, y1, 0)
    # 와니가 x=W로 찼을 때 궤적이 y=y1에서 도달하는 x좌표
    right = get_x_at_y(x, y, y1, W)

    if left > right:
        left, right = right, left

    # 골대 x범위와 궤적 범위의 교차 구간 계산
    gx1, gx2 = x1, x2  # x1 < x2 보장됨
    intersect_left = max(left, gx1)
    intersect_right = min(right, gx2)

    # 겹치는 구간의 길이 / W
    if intersect_left < intersect_right:
        prob = (intersect_right - intersect_left) / W
    else:
        prob = 0.0

    print(f"{prob:.10f}")
