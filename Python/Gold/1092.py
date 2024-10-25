import sys

input = sys.stdin.readline

n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)

m = int(input())
boxes = sorted(list(map(int, input().split())),reverse=True)

time = 0
if boxes[0] > cranes[0]:
    time = -1
else:
    while boxes:
        for c in cranes:
            if boxes and c < boxes[-1]:
                continue
            else:
                for b in boxes:
                    if b <= c:
                        boxes.remove(b)
                        break 
        time += 1
print(time)