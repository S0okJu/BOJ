import sys

input = sys.stdin.readline

def solution(cranes, boxes):
    time = 0
    # 1. 불가능한 경우 
    if cranes[0] < boxes[0]:
        time = -1
    else:
        while boxes:
            for crane in cranes:
                # 다음 크레인으로 넘기는 경우 
                if boxes and crane < boxes[-1]:
                    continue
                # 담는 경우 
                for box in boxes:
                    if crane >= box:
                        boxes.remove(box)
                        break
            
            time +=1
    
    print(time)
        
if __name__ == '__main__':
    n = int(input())
    cranes = sorted(list(map(int, input().split())), reverse=True)

    m = int(input())
    boxes = sorted(list(map(int, input().split())),reverse=True)

    solution(cranes, boxes)
